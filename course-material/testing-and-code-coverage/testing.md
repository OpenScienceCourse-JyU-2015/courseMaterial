# Testing and code coverage 

(Carlos Peña)

## Overview
* [What is unit testing?](#what-is-unit-testing?)
* [Why testing?](#why-testing?)
* [Create unit tests](#create-unit-tests)
* [Test-driven development](#test-driven-development)
* [Continuous integration](#continuous-integration)
* [Coverage](#coverage)


## What is unit testing?

From Wikipedia:
> In computer programming, **unit testing** is a software testing method by
> which individual units of source code, modules, usage procedures,
> and operating procedures, are tested to determine whether they are fit for use

The Clean Coder book by Uncle Bob:

![Clean coder book](img/clean_coder_book.png)

What Uncle Bob has to say about testing?:

![Clean coder book](img/clean_coder_book_testing1.png)

You got to be kidding me.

![Clean coder book](img/clean_coder_book_testing2.png)

## Why testing?
Large programs will have many components, units, that will depend from other
modules. There is a risk that modifications of one unit will affect the
behavior of other units, or models.

At the end of the day, after a hard day of programming, you can run your
unit test and if all pass then you can go home without any worries.

Touching code I wrote year ago that doesn't have unit tests.
![No testing](img/no_testing.gif)

## A magical command for IPython
**autoreload**: IPython extension to reload modules before executing user code.

Usage:

```python
%load_ext autoreload
%autoreload 2
```

## Create unit tests
We will use this repository <https://github.com/carlosp420/testing_repo>:

* Go to Github, log in.
* Fork this repository <https://github.com/carlosp420/testing_repo>
* Grab the repository URL <https://github.com/YOUR_NAME_OR_USERNAME/testing_repo.git>
* Clone the repository in your computer:

```shell
git clone https://github.com/YOUR_NAME_OR_USERNAME/testing_repo
cd testing_repo
```

We need to install the wonderful libraries ``nose`` and ``coverage``. Useful for
unit testing.

* Windows users: Put Python and scripts in your PATH. [Instructions](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday/Windows_set_up_Python).
* Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
* Install pip: ``python get-pip.py``
```shell
pip install nose
pip install coverage
```
* For Mac and Linux users:
```shell
sudo pip install nose
sudo pip install coverage
```

* Create one or more unit tests and save them to the file ``tests.py``
* Run the tests.

```shell
nosetests tests.py
```

* Write more tests. We always need more tests!

## Test-driven development
From Wikipedia:

> **Test-driven development (TDD)** is a software development process that relies
> on the repetition of a very short development cycle: first the developer 
> writes an (initially failing) automated test case that defines a desired 
> improvement or new function, then produces the minimum amount of code to pass
> that test.

## Continuous integration
From Wikipedia:
> **Continuous integration (CI)** is the practice, in software engineering, of
> merging all developer working copies with a shared mainline several times a day.
> CI was originally intended to be used in combination with automated unit
> tests written through the practices of test-driven development.

I say it is fancy wording for "testing with Github".

* We will go to the Travis CI webpage to read the documentation for setting up
  our repo in CI mode.
* Set up CI for our test-repo.
* Make a branch and see if Travis runs the tests.
* Add a badge to your README.md

## Coverage
* Measure test coverage:

```shell
nosetests tests.py --with-coverage --cover-html
```

* Setup your test-repo in coveralls.
* Configure Travis to work in combination with coveralls.
* For travis need to install:
```shell
sudo pip install coveralls
```
* Make a branch and see if Coveralls runs the tests.
* Add a badge to your README.md


Most scientists do not use any testing framework for their code:

![image by @quominus](img/unittests_in_cran.png)
