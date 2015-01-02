---
layout: post
title: "Hooking Up Android Gradle and Travis CI"
excerpt: "I’ve recently started using Gradle as the build system for my Android projects.  Travis CI is a very popular continuous integration tool for open source projects."
tags: [Android]
comments: true
image:
  feature: travis-logo_cover.png
---

I’ve recently started using [Gradle](http://www.gradle.org/) as the build system for my Android projects.  [Travis CI](https://travis-ci.org/) is a very popular continuous integration tool for open source projects.

### Hooking Up Travis CI to GitHub

To hook up Travis CI with Github, simply sign in using your GitHub account. Next, select which repos you want to hook up:

<p align="center">
  <img src="http://donnemartin.com/wp-content/uploads/2014/10/Screen-Shot-2014-10-04-at-4.21.59-AM.png">
</p>

Finally, add a .travis.yml file, such as the sample provided below, then push to kick off a build:

{% highlight yaml %}

android:
  components:
    # Uncomment the lines below if you want to
    # use the latest revision of Android SDK Tools
    # - platform-tools
    # - tools

    # The BuildTools version used by your project
    - build-tools-19.1.0

    # The SDK version used to compile your project
    - android-19

    # Additional components
    - extra-google-google_play_services
    - extra-google-m2repository
    - extra-android-m2repository
    - addon-google_apis-google-19

    # Specify at least one system image,
    # if you need to run emulator(s) during your tests
    - sys-img-armeabi-v7a-android-19
    - sys-img-x86-android-17

{% endhighlight %}

Depending on the load, Travis CI will then kick off a build and email you the results.

### Hooking Up Android Gradle to Travis CI

I found Travis CI to be difficult to integrate with Android Gradle from scratch, as the support is still in beta and there is a lack of documentation:

<p align="center">
  <img src="http://donnemartin.com/wp-content/uploads/2014/10/Screen-Shot-2014-10-03-at-7.45.20-PM-1024x263.png">
</p>

For example, I ran into the following cryptic issue:

<p align="center">
  <img src="http://donnemartin.com/wp-content/uploads/2014/10/Screen-Shot-2014-10-03-at-7.48.37-PM.png">
</p>

Which I fixed by adding the following to my .travis.yml:

{% highlight bash %}
chmod +x grailsw
{% endhighlight %}

Ultimately, a blank slate configuration of Android Gradle with Travis CI (in its current beta Android integration) proved to be quite a difficult task.  I decided to take a step back and evaluate other options.

### android-tdd-playground

[android-tdd-playground](https://github.com/donnemartin/android-tdd-playground) is a good starting point to enable your projects to use Gradle, Travis CI, and even the Android Testing Framework. I simply forked the project and started moving over components from my [Flickr Android app](https://github.com/donnemartin/photogallery) to the "playground" and customized as needed.

I recommend taking this approach when first starting with Travis CI, as it streamlines the integration and allows you to focus on your app.

### Travis CI Badge:

<p align="center">
  <img src="http://donnemartin.com/wp-content/uploads/2014/10/Screen-Shot-2014-10-03-at-7.48.37-PM.png">
</p>

The Travis CI badge gives visual feedback of the state of the last build.  Adding the Travis CI build results is just one line of code to your README markdown: [![Build Status](https://travis-ci.org/donnemartin/photogallery.svg?branch=master)](https://travis-ci.org/donnemartin/photogallery)

<p align="center">
  <img src="http://donnemartin.com/wp-content/uploads/2014/10/Screen-Shot-2014-10-04-at-4.39.06-AM.png">
</p>
