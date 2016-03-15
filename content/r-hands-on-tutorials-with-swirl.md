Title: R Hands-On Tutorials with Swirl
Date: 2014-12-09
Summary: Exploring R with the R package Swirl, which lets you learn right from the R console.
Tags: Data
CoverImage: https://raw.githubusercontent.com/donnemartin/donnemartin.github.io/master/images/posts/swirl.png
Thumbnail: http://i2.wp.com/donnemartin.net/wp-content/uploads/2014/12/swirl_featured-e1422795535586.png?zoom=2&resize=320%2C202

Coming from a Python data analysis background with SciPy, I have always been curious about R.

## Swirl

I decided to check out R and found a handy R package [swirl](http://swirlstats.com/). Swirl "teaches you R programming and data science interactively, at your own pace, and right in the R console".

## Installing Swirl from CRAN

The easiest way to install and run swirl is by typing the following commands in the R console:

```
install.packages("swirl")
library(swirl)
swirl()
```

## Lessons

Swirl comes with interactive lessons for the following R topics:

* Basic Building Blocks
* Sequences of Numbers
* Vectors
* Missing Values
* Subsetting Vectors
* Matrices and Data Frames
* Logic
* lapply and sapply
* vapply and tapply
* Looking at Data
* Simulation
* Dates and Times

You can also install the lessons described below from their [GitHub repo](https://github.com/swirldev/swirl_courses).

## Beginner Lessons

- **R Programming**: The basics of programming in R
- **Data Analysis**: Basic ideas in statistics and data visualization
- **Mathematical Biostatistics Boot Camp**: One- and two-sample t-tests, power, and sample size
- **Open Intro**: A very basic introduction to statistics, data analysis, and data visualization

## Intermediate Lessons

- **Regression Models**: The basics of regression modeling in R
- **Getting and Cleaning Data**: dplyr, tidyr, lubridate

## Advanced Lessons

- **Statistical Inference**: Introduces the student to basic concepts of statistical inference
including probability, hypothesis testing, confidence intervals and
p-values. It concludes with an initiation to topics of particular
relevance to big data, issues of multiple testing and resampling.

## Installing Additional Lessons

```
library(swirl)
install_from_swirl("Course Name Here")
swirl()
```

## Swirl in R Studio

Below is an output of the "Dates and Times" lesson:

<p align="center">
  <img src="http://donnemartin.net/wp-content/uploads/2014/12/swirl1.png" class="img-responsive">
</p>
