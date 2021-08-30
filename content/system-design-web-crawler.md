# Design a web crawler

*Note: This document links directly to relevant areas found in the [system design topics](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics) to avoid duplication.  Refer to the linked content for general talking points, tradeoffs, and alternatives.*

## Step 1: Outline use cases and constraints

> Gather requirements and scope the problem.
> Ask questions to clarify use cases and constraints.
> Discuss assumptions.

Without an interviewer to address clarifying questions, we'll define some use cases and constraints.

### Use cases

#### We'll scope the problem to handle only the following use cases

* **Service** crawls a list of urls:
    * Generates reverse index of words to pages containing the search terms
    * Generates titles and snippets for pages
        * Title and snippets are static, they do not change based on search query
* **User** inputs a search term and sees a list of relevant pages with titles and snippets  the crawler generated
    * Only sketch high level components and interactions for this use case, no need to go into depth
* **Service** has high availability

#### Out of scope

* Search analytics
* Personalized search results
* Page rank

### Constraints and assumptions

#### State assumptions

* Traffic is not evenly distributed
    * Some searches are very popular, while others are only executed once
* Support only anonymous users
* Generating search results should be fast
* The web crawler should not get stuck in an infinite loop
    * We get stuck in an infinite loop if the graph contains a cycle
* 1 billion links to crawl
    * Pages need to be crawled regularly to ensure freshness
    * Average refresh rate of about once per week, more frequent for popular sites
        * 4 billion links crawled each month
    * Average stored size per web page: 500 KB
        * For simplicity, count changes the same as new pages
* 100 billion searches per month

Exercise the use of more traditional systems - don't use existing systems such as [solr](http://lucene.apache.org/solr/) or [nutch](http://nutch.apache.org/).

#### Calculate usage

**Clarify with your interviewer if you should run back-of-the-envelope usage calculations.**

* 2 PB of stored page content per month
    * 500 KB per page * 4 billion links crawled per month
    * 72 PB of stored page content in 3 years
* 1,600 write requests per second
* 40,000 search requests per second

Handy conversion guide:

* 2.5 million seconds per month
* 1 request per second = 2.5 million requests per month
* 40 requests per second = 100 million requests per month
* 400 requests per second = 1 billion requests per month

## Step 2: Create a high level design

> Outline a high level design with all important components.

![Imgur](http://i.imgur.com/xjdAAUv.png)

## Step 3: Design core components

> Dive into details for each core component.

### Use case: Service crawls a list of urls

We'll assume we have an initial list of `links_to_crawl` ranked initially based on overall site popularity.  If this is not a reasonable assumption, we can seed the crawler with popular sites that link to outside content such as [Yahoo](https://www.yahoo.com/), [DMOZ](http://www.dmoz.org/), etc.

We'll use a table `crawled_links` to store processed links and their page signatures.

We could store `links_to_crawl` and `crawled_links` in a key-value **NoSQL Database**.  For the ranked links in `links_to_crawl`, we could use [Redis](https://redis.io/) with sorted sets to maintain a ranking of page links.  We should discuss the [use cases and tradeoffs between choosing SQL or NoSQL](https://github.com/donnemartin/system-design-primer#sql-or-nosql).

* The **Crawler Service** processes each page link by doing the following in a loop:
    * Takes the top ranked page link to crawl
        * Checks `crawled_links` in the **NoSQL Database** for an entry with a similar page signature
            * If we have a similar page, reduces the priority of the page link
                * This prevents us from getting into a cycle
                * Continue
            * Else, crawls the link
                * Adds a job to the **Reverse Index Service** queue to generate a [reverse index](https://en.wikipedia.org/wiki/Search_engine_indexing)
                * Adds a job to the **Document Service** queue to generate a static title and snippet
                * Generates the page signature
                * Removes the link from `links_to_crawl` in the **NoSQL Database**
                * Inserts the page link and signature to `crawled_links` in the **NoSQL Database**