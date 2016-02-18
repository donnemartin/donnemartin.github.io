Title: Under the Hood of SAWS, A Supercharged AWS CLI
Date: 2015-09-23
Summary: A brief look at some Python open source technologies used in SAWS.
Tags: Cloud, Data
CoverImage: https://camo.githubusercontent.com/2af72023269b0b320adf4ec55576435f5c8b79c4/687474703a2f2f692e696d6775722e636f6d2f767a43357a6d412e676966
Thumbnail: http://i0.wp.com/donnemartin.net/wp-content/uploads/2015/09/saws.png?zoom=2&resize=320%2C202

## What's SAWS?

[SAWS: GitHub Repo](https://github.com/donnemartin/saws)

## So what's under the hood?

### AWS CLI

Python-powered official [AWS CLI](https://github.com/aws/aws-cli).  Does the heavy lifting communicating with AWS and feeds completions to `SAWS`.  The AWS CLI uses [boto](https://github.com/boto/boto), the official Python SDK for AWS.

Check out [completer.py](https://github.com/donnemartin/saws/blob/master/saws/completer.py) for more details on how `awscli` is used.

### Python-Prompt Toolkit

[Python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) simplifies the creation of interactive command lines.

Used throughout the `SAWS` source code.

### Pygments

[Pygments](http://pygments.org/) is a syntax highlighter for `SAWS` commands and output.

Check out [lexer.py](https://github.com/donnemartin/saws/blob/master/saws/lexer.py) for more details on how `pygments` is used.

### Unit Tests

`SAWS` uses:

* [unittest](https://docs.python.org/2/library/unittest.html)
    * Check out the [tests](https://github.com/donnemartin/saws/tree/master/tests) folder
* [pexpect](https://pexpect.readthedocs.org/en/stable/)
    * Used in [test_cli.py](https://github.com/donnemartin/saws/blob/master/tests/test_cli.py) to run, interact, and stop the CLI
    * Not supported on Windows
* [Mock](https://pypi.python.org/pypi/mock)
    * Could be intimidating at first, here's a helpful [tutorial](http://www.toptal.com/python/an-introduction-to-mocking-in-python)

If you want to play around the development environment, run the following:

    $ git clone https://github.com/donnemartin/saws.git
    $ pip install -e .
    $ pip install -r requirements-dev.txt
    $ saws

Run unit tests in your active Python environment:

    $ python tests/run_tests.py

I'm also a fan of:

* [pytest](http://pytest.org/latest/)
* [nose](https://nose.readthedocs.org/en/latest/)

While working on `SAWS` I came across 'behavior driven development' with [behave](http://pythonhosted.org/behave/)--interesting!

### Tox

[Tox](https://tox.readthedocs.org/en/latest/) is used to automate and standardize testing in Python 2.6, 2.7, 3.3, 3.4, and pypy.

I've found Tox + [Travis CI](https://travis-ci.org/donnemartin/saws) to be a great combination.  To hook up tox to Travis CI, add the following to your [.travis.yml](https://github.com/donnemartin/saws/blob/master/.travis.yml):

    install:
      - travis_retry pip install tox

    after_success:
        - codecov

To run locally:

    $ tox

The [tox.ini](https://github.com/donnemartin/saws/blob/master/tox.ini) file specifies:

* Python environments
* Travis CI arguments
* Dependencies
* Test commands

### Coverage Tests

[![Codecov](https://img.shields.io/codecov/c/github/donnemartin/saws.svg)](https://codecov.io/github/donnemartin/saws/saws)

[Codecov](https://codecov.io/github/donnemartin/saws/saws) provides code coverage.  `SAWS` uses [codecov-python](https://github.com/codecov/codecov-python) to interact with CodeCov.

[Coveralls](https://coveralls.io/) is also very popular and can be used with [python-coveralls](https://github.com/z4r/python-coveralls) and [coveralls-python](https://github.com/coagulant/coveralls-python).

To hook up to Codecov to Travis CI, add the following to your [.travis.yml](https://github.com/donnemartin/saws/blob/master/.travis.yml):

    install:
      - pip install codecov

    after_success:
        - codecov

<p align="center">
  <img src="http://codecov.io/github/donnemartin/saws/branch.svg?branch=master" class="img-responsive">
</p>

### TravisCI

[![Build Status](https://travis-ci.org/donnemartin/saws.svg?branch=master)](https://travis-ci.org/donnemartin/saws)

[Travis CI](https://travis-ci.org/donnemartin/saws) provides continuous integration.

The [.travis.yml](https://github.com/donnemartin/saws/blob/master/.travis.yml) file specifies:

* Python versions
* OS (I had trouble getting Mac OS X to work)
* Install dependencies
* Script to run
* What to do after running (send the coverage stats to Codecov)

### Sphinx

[![Documentation Status](https://readthedocs.org/projects/saws/badge/?version=latest)](http://saws.readthedocs.org/en/latest/?badge=latest)

[Sphinx](http://sphinx-doc.org/) is a great documentation tool.  It takes your [docstrings](https://www.python.org/dev/peps/pep-0257/) and turns it into documentation that can be hosted on sites such as [Readthedocs.org](http://saws.readthedocs.org/en/latest/?badge=latest) and [PyPi](https://pypi.python.org/pypi/saws/).

Here's a handy article to learn more about how to build and upload your Sphinx docs to PyPi:

[](https://pythonhosted.org/an_example_pypi_project/buildanduploadsphinx.html)

Run the following to build the docs:

    $ python setup.py build_sphinx

### PyPI and Setup.py

[![PyPI version](https://badge.fury.io/py/saws.svg)](http://badge.fury.io/py/saws) [![PyPI](https://img.shields.io/pypi/pyversions/saws.svg)](https://pypi.python.org/pypi/saws/)

[Setup.py](https://github.com/donnemartin/saws/blob/master/setup.py) contains information on versioning, package requirements, and other useful info for [PyPI](https://pypi.python.org/pypi/saws).

This allows end-users to install with a one-liner:

    $ pip install saws

A `virtualenv` install is recommended to avoid potential permissions or package dependency issues.

Check out this [article](http://peterdowns.com/posts/first-time-with-pypi.html) to learn more about posting to PyPI.

### Git-Flow

[Git-Flow](https://github.com/nvie/gitflow) is a set of Git extensions that provide high-level repository operations for the popular [git branching model](http://nvie.com/img/git-model@2x.png).

### Misc

* [Six](https://pypi.python.org/pypi/six) - Python 2 and 3 compatibility.
* [Flake8](https://pypi.python.org/pypi/flake8) - Linter for code quality.
