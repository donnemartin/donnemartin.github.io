# Design Pastebin.com (or Bit.ly)

*Note: This document links directly to relevant areas found in the [system design topics](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics) to avoid duplication.  Refer to the linked content for general talking points, tradeoffs, and alternatives.*

**Design Bit.ly** - is a similar question, except pastebin requires storing the paste contents instead of the original unshortened url.

## Step 1: Outline use cases and constraints

> Gather requirements and scope the problem.
> Ask questions to clarify use cases and constraints.
> Discuss assumptions.

Without an interviewer to address clarifying questions, we'll define some use cases and constraints.

### Use cases

#### We'll scope the problem to handle only the following use cases

* **User** enters a block of text and gets a randomly generated link
    * Expiration
        * Default setting does not expire
        * Can optionally set a timed expiration
* **User** enters a paste's url and views the contents
* **User** is anonymous
* **Service** tracks analytics of pages
    * Monthly visit stats
* **Service** deletes expired pastes
* **Service** has high availability

#### Out of scope

* **User** registers for an account
    * **User** verifies email
* **User** logs into a registered account
    * **User** edits the document
* **User** can set visibility
* **User** can set the shortlink

### Constraints and assumptions

#### State assumptions

* Traffic is not evenly distributed
* Following a short link should be fast
* Pastes are text only
* Page view analytics do not need to be realtime
* 10 million users
* 10 million paste writes per month
* 100 million paste reads per month
* 10:1 read to write ratio

#### Calculate usage

**Clarify with your interviewer if you should run back-of-the-envelope usage calculations.**

* Size per paste
    * 1 KB content per paste
    * `shortlink` - 7 bytes
    * `expiration_length_in_minutes` - 4 bytes
    * `created_at` - 5 bytes
    * `paste_path` - 255 bytes
    * total = ~1.27 KB
* 12.7 GB of new paste content per month
    * 1.27 KB per paste * 10 million pastes per month
    * ~450 GB of new paste content in 3 years
    * 360 million shortlinks in 3 years
    * Assume most are new pastes instead of updates to existing ones
* 4 paste writes per second on average
* 40 read requests per second on average

Handy conversion guide:

* 2.5 million seconds per month
* 1 request per second = 2.5 million requests per month
* 40 requests per second = 100 million requests per month
* 400 requests per second = 1 billion requests per month

## Step 2: Create a high level design

> Outline a high level design with all important components.

![Imgur](http://i.imgur.com/BKsBnmG.png)

## Step 3: Design core components

> Dive into details for each core component.

### Use case: User enters a block of text and gets a randomly generated link

We could use a [relational database](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms) as a large hash table, mapping the generated url to a file server and path containing the paste file.

Instead of managing a file server, we could use a managed **Object Store** such as Amazon S3 or a [NoSQL document store](https://github.com/donnemartin/system-design-primer#document-store).

An alternative to a relational database acting as a large hash table, we could use a [NoSQL key-value store](https://github.com/donnemartin/system-design-primer#key-value-store).  We should discuss the [tradeoffs between choosing SQL or NoSQL](https://github.com/donnemartin/system-design-primer#sql-or-nosql).  The following discussion uses the relational database approach.

* The **Client** sends a create paste request to the **Web Server**, running as a [reverse proxy](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)
* The **Web Server** forwards the request to the **Write API** server
* The **Write API** server does the following:
    * Generates a unique url
        * Checks if the url is unique by looking at the **SQL Database** for a duplicate
        * If the url is not unique, it generates another url
        * If we supported a custom url, we could use the user-supplied (also check for a duplicate)
    * Saves to the **SQL Database** `pastes` table
    * Saves the paste data to the **Object Store**
    * Returns the url

**Clarify with your interviewer how much code you are expected to write**.
