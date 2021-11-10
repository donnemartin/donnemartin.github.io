# Design Amazon's sales rank by category feature

*Note: This document links directly to relevant areas found in the [system design topics](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics) to avoid duplication.  Refer to the linked content for general talking points, tradeoffs, and alternatives.*

## Step 1: Outline use cases and constraints

> Gather requirements and scope the problem.
> Ask questions to clarify use cases and constraints.
> Discuss assumptions.

Without an interviewer to address clarifying questions, we'll define some use cases and constraints.

### Use cases

#### We'll scope the problem to handle only the following use case

* **Service** calculates the past week's most popular products by category
* **User** views the past week's most popular products by category
* **Service** has high availability

#### Out of scope

* The general e-commerce site
    * Design components only for calculating sales rank

### Constraints and assumptions

#### State assumptions

* Traffic is not evenly distributed
* Items can be in multiple categories
* Items cannot change categories
* There are no subcategories ie `foo/bar/baz`
* Results must be updated hourly
    * More popular products might need to be updated more frequently
* 10 million products
* 1000 categories
* 1 billion transactions per month
* 100 billion read requests per month
* 100:1 read to write ratio
