Title: Debugging, testing and code profiling
Date: 2014-10-22
Summary: Debugging, testing and code profiling in Python
Status: hidden

# Debugging

- Basic technique: print statements, logging module
- Symbolic debugger
- Defensive programming, robustness, assert statement
- Silent errors are dangerous, need for rigorous testing

# Testing with Python

- Importance of testing (e.g. working code, modification, checking is needed to
  ensure that nothing broke)
- Manual testing with small test scripts
- Automated testing with unit tests
- Unit tests force to code small functions with one role, code easier to reuse
  and change
- Test-driven development: write the tests before the code

# Code coverage

- Tools for code coverage estimation
- Objective is 100% coverage, what is realistic, what is acceptable
- High coverage does not prove a code is correct

# Integration with Github

(this can also be exposed later, when documentation has been explained, as one
session about how to integrate testing, code coverage and documentation with
GitHub and ReadTheDocs)

- Automated testing with Travis
- Code coverage (is it also with Travis?)

# Profiling and refactoring

- There are several ways to do the same thing, all equally correct, but some
  are faster
- Code profiling tools
- Code timing, predicting run time for a given dataset size (useful to check
  that an analysis can be run in a reasonable amount of time and to estimate
  run times for CSC submissions)
- Basics of algorithmic complexity (constant time, n, n^2, trade-off memory and
  speed)
- General considerations when writing Python, guidelines for refactoring
- Interest of having a complete test suite before starting refactoring
