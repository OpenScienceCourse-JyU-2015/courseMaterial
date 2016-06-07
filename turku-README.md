Title: README working file
Date: 2014-10-22
Summary: README working file
Sortorder: 090
Status: hidden

(link to the course webpage: http://mdjbru-teaching-material.github.io/turku_course/)

### Table of content

* [Good templates for teaching software development](#good-templates-for-teaching-software-development)
    - [Software Carpentry](#software-carpentry)
    - [Other courses on Python](#other-courses-on-python)
* [Material to define the teaching objectives](#material-to-define-the-teaching-objectives)
    - [Important concepts to teach](#important-concepts-to-teach)
* [Comments](#comments)
    - [Choosing Python or R?](#choosing-python-or-r)
* [Project draft](#project-draft)
    - [Timeline and practical organization](#timeline-and-practical-organization)
    - [General contents](#general-content)
	- [Prerequisites](#prerequisites)
	- [Detailed contents](#detailed-content)
	- [Teachers](#teachers)

## Good templates for teaching software development

### Software Carpentry

Unix shell, Git and R (we can replace R with Python)
    <https://github.com/karthik/2014-10-31-nw>.

They are using a Creative Commons license. So we can use the material, remix it
but need to give credits.

There is also a very nice example of how to use Dropbox public links to share
scripts and bash history live with students
<http://software-carpentry.org/blog/2015/02/instructor-debriefing-2015-02-10.html>.

### Other courses on Python

There are many here <https://wiki.python.org/moin/PythonTraining>. We can
cherry-pick from there. It seems that a ovewiew course including
test-driven-development (TDD)and other best-practices are not too common? Maybe
not for very beginners maybe.

One option could be to teach the very basics of Python from the
"best-practices" approach. (Pep8 and TDD).

## Material to define the teaching objectives

The points we want to teach will depend on the expected audience level
(beginner, proficient user, advanced) an also of course on our own skills!

This blog <http://sijinjoseph.com/programmer-competency-matrix/> gives a good
view of programming skills at different stages of a programmer learning
life. Maybe we can use it as a basis to select what to teach to which audience?

There is also this site
<http://www.wayland-informatics.com/The%20Seven%20Stages%20of%20Expertise%20in%20Software.htm>.

### Important concepts to teach

(see also the Software Carpentry materials)

* To complete beginners (i.e. people would never used Python or R):
  - introduction to a programming language (Python, R or even just the bash
  shell)
  - automation of repeated tasks by writing scripts (again, using Python, R or
the bash)
  - version controlling of scripts
  - working remotely (e.g. bash shell on CSC)
  - integration of Git with Github/Bitbucket. Pull requests.
  - Workflows
    (e.g. [here](http://blog.shvetsov.com/2013/04/using-git-with-dropbox.html)
    and
    [here](http://jetheis.com/blog/2013/02/17/using-dropbox-as-a-private-github/)
    for non- or not-yet public scripts via Dropbox/Bitbucket
  - Git for "Single Developer" (e.g.
  [this](http://nvie.com/posts/a-successful-git-branching-model/) and
  [this](http://octodecillion.com/blog/single-developer-git-workflow/))
  - Or this:
  ![http://xkcd.com/1296/](http://imgs.xkcd.com/comics/git_commit.png)
  
* To more experienced users:
  - virtual environments
  - testing, coverage and test-driven development
  - Continuous Integration testing with [Travis](https://travis-ci.org/).
  - Automatic documentation on the web with
    [Read the Docs](https://readthedocs.org/).
  - python module packaging. Submitting packages to the
    [Python Package Index](https://pypi.python.org/).
  - debugging (symbolic debugger) (a good
    [resource](http://blog.ionelmc.ro/2013/06/05/python-debugging-tools/) for
    Python)
  - code profiling
  
## Comments

Carlos talked to Niklas. It seems the department really needs PhD courses as
students have hard time finding course to get credits from. Besides there might
be funding available for such PhD course (need to talk to Ville). Then this
course can be open to postdocs as well. In such case, it is likely that many
students will be experienced.  We can aim for giving the course January or
February. So there is time for advertise it.  If it is a PhD course (preferred
option for both Carlos and Matthieu) then it can be a three-day full day
course. If it is aimed for master students then it should be once a week maybe
(as they have many other activities during the week).

There is a Master's program at UTU on
[Bioinformatics](https://nettiopsu.utu.fi/opas/tutkintoOhjelma.htm?rid=22413&uiLang=fi&lang=en&lvv=2014).
It seems that there is no course on "best-practices" such as version control or
unittesting.

It might be a good idea to be precise about what prerequisites we
expect. If we need to cover the basics of R/Python we might not have
the time to get to the meat of the course.

### Choosing Python or R?

It might be too audacious to aim at teaching both Python and R during only 3
days. Maybe it would be more reasonable to choose only one, and use it to teach
the concepts (functions, modular code, version control, testing, ...).

* **Python**
  - **pros**
    - widely used, lots of scientific libraries, including matplotlib, numpy, pandas
    - clean syntax, easy to learn
	- nice modules for testing and code coverage
	- documentation can easily be included as docstrings in the code
  - **cons**
    - maybe not the most useful for biology Ph.Ds: they are more likely to have
      to do analyses in R than to do data processing in Python. Even if pandas
      is there in Python, Matthieu thinks R is probably the tool of choice when
      it comes to statistical analyses.
    - there are currently two main versions of Python, can be a bit
      confusing. One way could be just to use version 3 and just mention
      version 2 without going back to it during the course.
	- not a single mainstream IDE equivalent to RStudio with R?
* **R**
  - **pros**
    - simple language, widely used, with a very large package library
	- there are frameworks for testing (e.g. testthat) and writing modules
    easily (e.g. devtools)
	- RStudio is a nice IDE and has integrated interaction with Git
	- nice profiling and benchmark tools
  - **cons**
    - maybe not as "clean" language as Python (for example, the methods for
      classes are less visible than in Python, and object-oriented programming
      might be more confusing to learn).
	- not proper coverage tools yet (even though some tools exist).

In short: Python more adapted for teaching informatic concepts, R more adapted
for biologists?

One way can be to give the course with Python: once the concepts are learnt and
adopted, they can be easily transferred to R. Also, Ph.D students are more
likely to be exposed to R at some point in some other course (isn't there
already an R course for Ph.D at Utu actually?).

It could be also good to have a follow-up course focusing on R.

## Project draft

This is a basic project draft, aiming at a PhD course.

### Timeline and practical organization

* It might be good to set up a web page on GitHub to present the course and the
  practical details, as well as make the teaching material available. Software
  Carpentry has a [GitHub repository](https://github.com/swcarpentry/bc) which
  explains how to do it. It would be nice to generate it with a Python static
  site generator ([Jekyll](http://jekyllrb.com/), which is the static site
  generator of choice for GitHub, is written in Ruby!), and
  [Pelican](http://docs.getpelican.com/en/3.4.0/index.html) might be a good
  choice for that. It uses [Pygments](http://pygments.org/) for code syntax
  highlighting. A detailed explanation about how to publish on GitHub with
  Pelican is available [here](http://docs.getpelican.com/en/3.4.0/tips.html).

* A draft version of the website is available here:
  http://mdjbru-teaching-material.github.io/turku_course/

* Course duration: 3 full days. Possibilities are:
    - **Three consecutive days**. Advantages: compact, people can focus on the
    course and the material from a given day is still fresh the next
    day. Inconvenient: people do not have time to apply what they learn to
    their own research in-between classes and it is less likely that we get
    feedback from one day to the other. Also, if people do not try to apply
    what they learn at once after the classes, they might just forget about it
    and the course will be of little use.
    - **One full day per week during three consecutive weeks**. Advantages:
    people only have to focus one day at a time, they do not accumulate fatigue
    about informatics during three consecutive days and they are more likely to
    be fresh and rested before each teaching day. People have time between each
    week to try the things they learn, and come back with questions on the next
    session. People are "re-activated" about applying what they learn three
    separate times, and it is more likely that they will try to apply what they
    learn just after hearing about it if they have three opportunities instead
    of just one in hte case of a consecutive three-day course. Inconvenient:
    people have to be available for one day in three consecutive weeks, might
    be a bit harder to fit in their schedule. Also people might tend to forget
    a bit more about what they heard the previous time (but this is probably
    not a big problem since a quick reminder can be done at the beginning of
    each day, and the material will probably be divided in more or less
    independent units over the three days), but this can be counter-balanced by
    the advantage of having more time to incorporate and train on the previous
    topics during each week.

* Teachers involved:
    - Matthieu
    - Carlos
    - Roland
    - we can also check with Tiina if she would be interested in teaching
    something there?
    - other researchers of the group (e.g. Erica and NGS specific things? She
    has been giving workshops in 2011 in Jyväskylä and in 2014 in Roscoff).

* Place and practicals
    - Depends on the number of people attending, maybe a reasonable expectation
    is 5-30?
    - Genetics seminar room  or similar is ideal. Niklas said that the Genetics
    seminar room is free of charge for us while we would need to rent some
    other lecture room (for example those in LT1).
    Small room and video projector, internet access through Sparknet, students
    can easily chat with each other to solve issues and it is easy for the
    teacher (and potential helpers) to walk between the tables and help
    students individually.
    - Each course is probably a mix of presentation on the screen and
    practicals (hopefully more practicals than lecture-like presentation), and
    it would be good to have, in addition to the teacher, one or two helpers to
    assist for the practicals (Matthieu was participating in Erica's
    bioinformatics workshop in Jyväskylä in 2011 and in his experience it was
    extremely helpful to have several people helping the students with the
    practicals in addition to the main teacher).

* Persistency of teaching materials (github, pdf, presentations, links to
  online references)

* Aim is not to teach everything but to deliver the important concepts
  (e.g. version control, testing) and the basic skills (shell, git basics, data
  persistence and traceability, programming, debugging) so that they can learn
  by themselves and adopt good practices when using other tools (e.g. teaching
  how to use CSC might not be feasible in three days, but if they now how to
  use the shell, how to connect remotely, how to transfer files and to version
  control their scripts they are well equipped and can deal with the very good
  documentation of CSC).
	   
* CSC accounts for students? See with Erica how it was working for the
  Jyväskylä bioinformatics course in 2011. We can actually check with her if
  there is still material available on-line for that and how were the
  practicals for using CSC accounts for students.

* Note: CSC use a module system which might be a bit hard to grasp at the
  beginning, but if virtual environments are already introduced to the students
  then it is probably very easy to understand.

* Feedback form one month or six month after the course to see if people have
  changed their habits?

### General contents

* Main objectives (from the Software Carpentry website):
    - "to make scientists more productive, and their work more reliable, by
    teaching them basic computing skills."
    - "most scientists are never taught how to build, use, validate, and share
    software well. As a result, many spend hours or days doing things badly
    that could be done well in just a few minutes. Our goal is to change that
    so that scientists can spend less time wrestling with software and more
    time doing useful research."

* In this respect, the objectives are probably more about **giving basic, solid
  computer skills** than can be invested into research projects afterwards
  rather than teaching how to analyse NGS data *per se*.

* Again from Software Carpentry, the core topics:
    - the basics of structured programming in Python or R
    - version control using Git, Mercurial, or Subversion
    - unit testing using an xUnit-style framework
    - automating tasks using the Unix shell

* Each concept taught can be illustrated by a real-life example for
  scientists. It is fairly easy to take examples from our real research
  experience and give it to the students as a training.

### Prerequisites

* Realistically, we cannot expect all students to have experience with even
  basic programming. Some will probably have used R but not all, while a few
  can be already experienced in Python and R.

* Safe to assume that everybody is beginner and familiar only with Windows or
  Mac environment.

* We have to ensure that every concept taught can be understood based on was is
  explained before.

* We should ask students when they register what is their expertise in
  informatics, if they already use any programming language, what is their
  operating system, if they have been using the CSC services or not. A good
  starting point is from the Software Carpentry materials
  [here](http://software-carpentry.org/workshops/assess/pre-learner.html).

### Short contents

* Introduction to python
* Version control with Git
* Sharing code (GitHub and BitBucket)
* Introduction to the shell
* Test and code coverage
* Code profiling
* Debugging
* Documentation
* Virtual environments
* Pet project

### Detailed contents

* Day one, morning: **scripting and version control**
    - introduction to scripting language (Python or R)
    - basic variable assignment, flow control
    - functions
    - writing modulable and re-usable code

* Day one, afternoon: **scripting and version control**
    - finishing scripting
    - version control with Git (this probably depends on having introduced a
    scripting language before, either bash or R or Python)
    - Git for single developper
    - Sharing code with GitHub or BitBucket (a word about licenses?)
	- It would be nice to illustrate the use of GitHub and BitBucket by showing
      real-life projects that use them (e.g. BioPython, ggplot2, ...)
	- **note**: since most students probably don't use a Linux environment on
      their laptop, it could be a good move to introduce a GUI for Git (there
      is a list [here](http://git-scm.com/download/gui/linux)). Git also comes
      with ``git-gui`` and ``gitk``, which could be used instead of a
      third-party tool to keep things simple and to avoid introducing another
      tool. Using Git from the command line could be done later. Or is it that
      the command line use should be presented at once? On the one hand, it
      might be good to get students used as soon as possible to using the
      command line version, but on the other hand they might never use Git if
      we start with an abrupt introduction Git + command line.

* Day two, morning: **bash shell and task automation, ssh**
    - working remotely: ssh to CSC
    - introduction to bash shell (important for e.g. CSC)
    - automation of repeated tasks with shell scripts (for Windows users, what
    about win-bash, cygwin or UnxUtils?)

* Day two, afternoon: **testing and code profiling**
    - testing, coverage with either Python or R
    - debugging (print statements, symbolic debuggers, ``traceback()`` and
    ``recover()`` in R)
    - code profiling, refactoring (underline the interest of having a test
    suite ready when improving a code that already works)
	- if enough time, code timing (i.e. try to predict how long code will take
      to run by running small subsets, looking at the relationship between
      input size and run time and extrapolating). This might be especially
      useful when preparing a parallel run on CSC for example, or just to know
      how much can be done in a given time.

* Day three, morning: **documentation and virtual environments**
    - docstrings in Python, basics of R package writing
    - basics of Python module writing
    - interest and use of virtual environments

* Day three, afternoon: **if time, integrated pet project?**
    - would be nice if students could decide on a common pet project at the end
    of day two
    - the afternoon could be used to divide the works between small teams
    (e.g. each team has to write a couple of functions, for which the input and
    output matches the other teams functions to produce a complete module or
    pipeline)
    - people would have to write simple code, test for it, documentation and
    publish it on GitHub

### Teachers

| Day | Topic                            | kept | Proposed teacher |
|-----|----------------------------------|------|------------------|
|   1 | Intro to Python                  | x    | Carlos           |
|   1 | Intro to R                       |      | Matthieu         |
|   1 | Version control with Git         | x    | Matthieu         |
|   1 | Git, single developper           | x    | Matthieu         |
|   1 | Sharing code with GitHub         | x    | Carlos           |
|   2 | Bash shell, ssh, task automation | x    | Matthieu         |
|   2 | Testing, code coverage           | x    | Carlos           |
|   2 | Debugging                        | x    | Matthieu         |
|   2 | Code profiling                   | x    | Matthieu         |
|   3 | Documentation, modules in Python | x    | Carlos           |
|   3 | Writing R packages               |      | Matthieu         |
|   3 | Virtual environments             | x    | Carlos           |

Teaching per person:

* Carlos: 5
* Matthieu: 5
* Roland: none, but willing to participate in material preparation

Roland is not sure that he will be available in February 2015 to actually
participate in the teaching, but he is willing to participate in the material
preparation (especially in the Python documentation part).

### Other

Should we talk a bit about licenses?

Maybe we could use [Etherpad](http://etherpad.org) to share code during the
sessions? There is a list of public instances
[here](https://github.com/ether/etherpad-lite/wiki/Sites-that-run-Etherpad-Lite).
