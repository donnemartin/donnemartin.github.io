---
layout: post
title: "A Brief Introduction to R Unit Testing with test_that"
excerpt: "Testing is a vital part of software development.  I've recently hooked up test_that to my R-Snippets repo."
tags: [Data]
comments: true
image:
  feature: Rlogo-1_cover.png
---

Testing is a vital part of software development.  I've always been an advocate of Test Driven Development (TDD) and use [nose](https://nose.readthedocs.org/en/latest/) for my python data analysis projects.  I've recently hooked up [test_that](http://cran.r-project.org/web/packages/testthat/index.html) to my [R Snippets Repo](https://github.com/donnemartin/r-snippets).

## Installing test_that

The easiest way to install and run test_that is by typing the following commands in the R console:

{% highlight r %}
install.packages("devtools")
library(devtools)
{% endhighlight %}

To set up your package to use testthat, run:

{% highlight r %}
devtools::use_testthat()
{% endhighlight %}

This creates a tests/testthat/ directory where tests live.  It also updates the [DESCRIPTION](https://github.com/donnemartin/r-snippets/blob/master/DESCRIPTION) file.

Tests are organised hierarchically:

* Expectations are grouped into tests
* Tests are organised in files

## Running Tests

To execute tests, run:

{% highlight r %}
devtools::test()
{% endhighlight %}

To skip a test, add the following within the test_that function body:

{% highlight r %}
skip("reason for skipping")
{% endhighlight %}

## Expectations

* **expect_true(x)**  checks that an expression is true.
* **expect_false(x)** checks that an expression is false.
* **expect_is(x, y)** checks that an object inherit()s from a specified class
* **expect_equal(x, y)**  check for equality with numerical tolerance
* **expect_equivalent(x, y)** a more relaxed version of equals() that ignores attributes
* **expect_identical(x, y)**  checks for exact equality
* **expect_matches(x, y)**    matches a character vector against a regular expression.
* **expect_output(x, y)** matches the printed output from an expression against a regular expression
* **expect_message(x, y)**    checks that an expression shows a message
* **expect_warning(x, y)**    expects that you get a warning
* **expect_error(x, y)**  verifies that the expression throws an error.

## Special Considerations

test_that does a good job ensuring that each test is run in its own environment and is self-contained.

The test_that documentation lists the following as exceptions:

* The filesystem: creating and deleting files, changing the working directory, etc.
* The search path: library(), attach().
* Global options, like options() and par().

## Code Snippets

The following abbreviated snippets of code test loading real world data sets from various sources to R.  The full source can be found in the [R Snippets Repo](https://github.com/donnemartin/r-snippets).

Test whether a file was downloaded:

{% highlight r %}
context("Reading Data")  # A context is a human readable file name
...
test_that("data is downloaded from URL", {
  fileDataUrl <- paste("https://d396qusza40orc.cloudfront.net/",
                       "getdata%2Fdata%2Fss06pid.csv",
                       sep="")
  fileDataDest <- "getdata-data-restaurants.xml"
  DownloadDataFromUrl(fileDataUrl,
                      fileDataDest)
  expect_true(file.exists(fileDataDest))
})

{% endhighlight %}

Test whether a computed result is the same as the baseline result:

{% highlight r %}
...
test_that("data on number of baltimore restaurants by zip is read from xml", {
  zip <- 21217
  result <- NumBaltimoreRestaurants(zip)
  baseline <- 32
  expect_equal(result, baseline)
})

{% endhighlight %}

Test whether a computed result is the same as the baseline result, with a tolerance:

{% highlight r %}
...
test_that("data on mean person weight replicate is read using sqldf", {
  result <- MeanProbabilityWeight()
  baseline <- 103.8886
  tolerance <- 10
  expect_equal(result, baseline, tolerance)
})

{% endhighlight %}