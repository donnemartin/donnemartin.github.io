---
layout: post
title: "Exploring R with Swirl"
excerpt: "Exploring R with the R package Swirl, which lets you learn right from the R console."
tags: [Data]
comments: true
---

Coming from a Python data analysis background with SciPy, I have always been curious about R.

I decided to check out R and found a handy R package [swirl](http://swirlstats.com/). Swirl "teaches you R programming and data science interactively, at your own pace, and right in the R console".

## Installing swirl (from CRAN)

The easiest way to install and run swirl is by typing the following from the R console:

{% highlight r %}
install.packages("swirl")
library(swirl)
swirl()
{% endhighlight %}

![alt text](http://donnemartin.com/wp-content/uploads/2014/12/swirl1.png)