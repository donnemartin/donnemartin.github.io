# Design Mint.com

*Note: This document links directly to relevant areas found in the [system design topics](https://github.com/donnemartin/system-design-primer#index-of-system-design-topics) to avoid duplication.  Refer to the linked content for general talking points, tradeoffs, and alternatives.*

## Step 1: Outline use cases and constraints

> Gather requirements and scope the problem.
> Ask questions to clarify use cases and constraints.
> Discuss assumptions.

Without an interviewer to address clarifying questions, we'll define some use cases and constraints.

### Use cases

#### We'll scope the problem to handle only the following use cases

* **User** connects to a financial account
* **Service** extracts transactions from the account
    * Updates daily
    * Categorizes transactions
        * Allows manual category override by the user
        * No automatic re-categorization
    * Analyzes monthly spending, by category
* **Service** recommends a budget
    * Allows users to manually set a budget
    * Sends notifications when approaching or exceeding budget
* **Service** has high availability

#### Out of scope

* **Service** performs additional logging and analytics

### Constraints and assumptions

#### State assumptions

* Traffic is not evenly distributed
* Automatic daily update of accounts applies only to users active in the past 30 days
* Adding or removing financial accounts is relatively rare
* Budget notifications don't need to be instant
* 10 million users
    * 10 budget categories per user = 100 million budget items
    * Example categories:
        * Housing = $1,000
        * Food = $200
        * Gas = $100
    * Sellers are used to determine transaction category
        * 50,000 sellers
* 30 million financial accounts
* 5 billion transactions per month
* 500 million read requests per month
* 10:1 write to read ratio
    * Write-heavy, users make transactions daily, but few visit the site daily
