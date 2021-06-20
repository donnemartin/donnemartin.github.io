# Design the Twitter timeline and search

*Note: This document links directly to relevant areas found in the [system design topics](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics) to avoid duplication.  Refer to the linked content for general talking points, tradeoffs, and alternatives.*

**Design the Facebook feed** and **Design Facebook search** are similar questions.

## Step 1: Outline use cases and constraints

> Gather requirements and scope the problem.
> Ask questions to clarify use cases and constraints.
> Discuss assumptions.

Without an interviewer to address clarifying questions, we'll define some use cases and constraints.

### Use cases

#### We'll scope the problem to handle only the following use cases

* **User** posts a tweet
    * **Service** pushes tweets to followers, sending push notifications and emails
* **User** views the user timeline (activity from the user)
* **User** views the home timeline (activity from people the user is following)
* **User** searches keywords
* **Service** has high availability

#### Out of scope

* **Service** pushes tweets to the Twitter Firehose and other streams
* **Service** strips out tweets based on users' visibility settings
    * Hide @reply if the user is not also following the person being replied to
    * Respect 'hide retweets' setting
* Analytics

### Constraints and assumptions

#### State assumptions

General

* Traffic is not evenly distributed
* Posting a tweet should be fast
    * Fanning out a tweet to all of your followers should be fast, unless you have millions of followers
* 100 million active users
* 500 million tweets per day or 15 billion tweets per month
    * Each tweet averages a fanout of 10 deliveries
    * 5 billion total tweets delivered on fanout per day
    * 150 billion tweets delivered on fanout per month
* 250 billion read requests per month
* 10 billion searches per month

Timeline

* Viewing the timeline should be fast
* Twitter is more read heavy than write heavy
    * Optimize for fast reads of tweets
* Ingesting tweets is write heavy

Search

* Searching should be fast
* Search is read-heavy

#### Calculate usage

**Clarify with your interviewer if you should run back-of-the-envelope usage calculations.**

* Size per tweet:
    * `tweet_id` - 8 bytes
    * `user_id` - 32 bytes
    * `text` - 140 bytes
    * `media` - 10 KB average
    * Total: ~10 KB
* 150 TB of new tweet content per month
    * 10 KB per tweet * 500 million tweets per day * 30 days per month
    * 5.4 PB of new tweet content in 3 years
* 100 thousand read requests per second
    * 250 billion read requests per month * (400 requests per second / 1 billion requests per month)
* 6,000 tweets per second
    * 15 billion tweets per month * (400 requests per second / 1 billion requests per month)
* 60 thousand tweets delivered on fanout per second
    * 150 billion tweets delivered on fanout per month * (400 requests per second / 1 billion requests per month)
* 4,000 search requests per second
    * 10 billion searches per month * (400 requests per second / 1 billion requests per month)

Handy conversion guide:

* 2.5 million seconds per month
* 1 request per second = 2.5 million requests per month
* 40 requests per second = 100 million requests per month
* 400 requests per second = 1 billion requests per month

## Step 2: Create a high level design

> Outline a high level design with all important components.

![Imgur](http://i.imgur.com/48tEA2j.png)

## Step 3: Design core components

> Dive into details for each core component.

### Use case: User posts a tweet

We could store the user's own tweets to populate the user timeline (activity from the user) in a [relational database](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms).  We should discuss the [use cases and tradeoffs between choosing SQL or NoSQL](https://github.com/donnemartin/system-design-primer#sql-or-nosql).

Delivering tweets and building the home timeline (activity from people the user is following) is trickier.  Fanning out tweets to all followers (60 thousand tweets delivered on fanout per second) will overload a traditional [relational database](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms).  We'll probably want to choose a data store with fast writes such as a **NoSQL database** or **Memory Cache**.  Reading 1 MB sequentially from memory takes about 250 microseconds, while reading from SSD takes 4x and from disk takes 80x longer.<sup><a href=https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know>1</a></sup>

We could store media such as photos or videos on an **Object Store**.

* The **Client** posts a tweet to the **Web Server**, running as a [reverse proxy](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)
* The **Web Server** forwards the request to the **Write API** server
* The **Write API** stores the tweet in the user's timeline on a **SQL database**
* The **Write API** contacts the **Fan Out Service**, which does the following:
    * Queries the **User Graph Service** to find the user's followers stored in the **Memory Cache**
    * Stores the tweet in the *home timeline of the user's followers* in a **Memory Cache**
        * O(n) operation:  1,000 followers = 1,000 lookups and inserts
    * Stores the tweet in the **Search Index Service** to enable fast searching
    * Stores media in the **Object Store**
    * Uses the **Notification Service** to send out push notifications to followers:
        * Uses a **Queue** (not pictured) to asynchronously send out notifications

**Clarify with your interviewer how much code you are expected to write**.

If our **Memory Cache** is Redis, we could use a native Redis list with the following structure:

```
           tweet n+2                   tweet n+1                   tweet n
| 8 bytes   8 bytes  1 byte | 8 bytes   8 bytes  1 byte | 8 bytes   8 bytes  1 byte |
| tweet_id  user_id  meta   | tweet_id  user_id  meta   | tweet_id  user_id  meta   |
```

The new tweet would be placed in the **Memory Cache**, which populates the user's home timeline (activity from people the user is following).

We'll use a public [**REST API**](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest):

```
$ curl -X POST --data '{ "user_id": "123", "auth_token": "ABC123", \
    "status": "hello world!", "media_ids": "ABC987" }' \
    https://twitter.com/api/v1/tweet
```

Response:

```
{
    "created_at": "Wed Sep 05 00:37:15 +0000 2012",
    "status": "hello world!",
    "tweet_id": "987",
    "user_id": "123",
    ...
}
```

For internal communications, we could use [Remote Procedure Calls](https://github.com/donnemartin/system-design-primer#remote-procedure-call-rpc).

### Use case: User views the home timeline

* The **Client** posts a home timeline request to the **Web Server**
* The **Web Server** forwards the request to the **Read API** server
* The **Read API** server contacts the **Timeline Service**, which does the following:
    * Gets the timeline data stored in the **Memory Cache**, containing tweet ids and user ids - O(1)
    * Queries the **Tweet Info Service** with a [multiget](http://redis.io/commands/mget) to obtain additional info about the tweet ids - O(n)
    * Queries the **User Info Service** with a multiget to obtain additional info about the user ids - O(n)

REST API:

```
$ curl https://twitter.com/api/v1/home_timeline?user_id=123
```

Response:

```
{
    "user_id": "456",
    "tweet_id": "123",
    "status": "foo"
},
{
    "user_id": "789",
    "tweet_id": "456",
    "status": "bar"
},
{
    "user_id": "789",
    "tweet_id": "579",
    "status": "baz"
},
```
### Use case: User views the user timeline

* The **Client** posts a user timeline request to the **Web Server**
* The **Web Server** forwards the request to the **Read API** server
* The **Read API** retrieves the user timeline from the **SQL Database**

The REST API would be similar to the home timeline, except all tweets would come from the user as opposed to the people the user is following.
