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
