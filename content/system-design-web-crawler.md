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
