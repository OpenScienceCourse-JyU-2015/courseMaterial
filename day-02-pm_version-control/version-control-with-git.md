Before the course
-----------------

Prerequisites:

-   a basic knowledge of the **Unix shell** (cf. day one of bootcamp)

After the course
----------------

After completing this course you will know:

-   what is version control and what it can do for you
-   how to set up a new repository for your project
-   how to track files, commit changes and view their history
-   how to revert to a previous state of your project
-   how to share your code publicly

1. Introduction to version control
==================================

1.1 A common problemm
---------------------

-   Some common issues arise when files are not version-controlled:

*images/phd052810s.png*

*images/phd\_notfinal.gif*

-   This happens not only for data or manuscripts, but for
    scripts also... How can we do it better?

1.2 Reproducibility of research?
--------------------------------

-   Research should be reproducible by others.
-   This refers to the experiments generating the data, but also to the
    analysis of the data.
-   The first researcher who will need to reproduce your results is
    likely to be **you**.

A lab notebook for files?

-   Lab books make lab work traceable. Analyses should also
    be traceable.
-   Analysis steps must be recorded, and reverting to any previous step
    must be possible.
-   This ensures that we always exactly know how a result was generated.

1.3 A possible solution: version control
----------------------------------------

-   **Version control** is a tool to **keep track of file changes**.
-   However, version control softwares offer more than simply recording
    successive versions of a file.
-   Version controlled projects can be **forked**, **merged** and
    **shared with collaborators**.
-   Interesting both for **collaborative work** and for **single
    researcher**

1.4 Example of a version control flow for a Python script
---------------------------------------------------------

*images/version-control-workflow.gif*

-   **V1**, **V2**, and **V3** are successive versions of the script
-   **V4** is committed, but then a mistake is found. We revert to
    **V3**
-   A new, correct **V4** is committed
-   **V5** and **V6** are successive versions of the script
-   At this point, we want to implement a new feature that might be
    interesting, but which is experimental. In order to keep **V6**
    clean, we create a new branch in which we can experiment with the
    script without damaging the stable **V6**
-   **V6b** and **V7b** are successive versions of the experimental
    script
-   At some point, the experimental changes are mature and we want to
    merge them back into the master branch. **V7b** and **V6** are
    merged together into **V8**
-   We realise we want to revert to a previous version of one function
    in the script. For this function, we revert to the code present in
    **V2**, keep all the rest as it is in **V8** and commit it as **V9**
-   **V10** is the next commit

1.5 What are the available tools?
---------------------------------

-   Existing version control tools
    -   [Subversion](https://subversion.apache.org/)
    -   [Bazaar](http://bazaar.canonical.com/en/)
    -   [Mercurial](http://mercurial.selenic.com/)
    -   [Git](http://git-scm.com/), which is one of the most popular
        ones nowadays
-   Online servers for repositories
    -   [BitBucket](https://bitbucket.org/) (free private repositories)
    -   [GitHub](https://github.com) (free for public repositories but
        not for private repositories)

2 Set up your project folder
============================

-   We want to write a book of recipes. We decide to create a folder to
    hold all our recipes, with one file for each recipe.

-   We will use Git to track the changes in our recipe folder.

-   You will first learn how to use Git with the command line to
    understand how it works. Later, you can use one of the numerous Git
    graphical user interfaces to use Git with your projects.

2.1 Connect to the server
-------------------------

-   Log into the remote server using `ssh` (GNU/Linux or Mac) or
    `putty` (Windows)

-   For `ssh` connection:

    ``` {.bash}
    ssh jyybioxx@130.234.109.113
    ```

-   Username: `jyybioxx`

-   Password: on the whiteboard!

2.2 Create your project folder
------------------------------

-   Create a new folder for your recipes

    ``` {.bash}
    mkdir recipes
    # Go into the new folder
    cd recipes
    ```

-   Create an empty file for this week report:

        touch pancakes

2.3 Write some text
-------------------

-   Edit your file with `nano`. Nano is a basic text editor which can be
    used from the command line.

-   Nano usage:
    -   `nano pancakes` to start editing
    -   Type text as you wish
    -   Use arrows to move around your text
    -   Press `CTRL + O` to save your edited text
    -   Press `CTRL + X` to exit
-   Fill in some text for the three first days of the week:

    ``` {.example}
    Pancake recipe

    Ingredients:
     500g of flour
     5 eggs
     1 liter of milk
    ```

-   Save your edited file and go back to the command line prompt.

3 Git basics (1) - Tracking files and committing changes
========================================================

3.1 Initialize a Git repository
-------------------------------

-   Now we are ready to track our report file. First we need to initiate
    a Git repository in our project folder:

    ``` {.bash}
    # Make sure the current folder is the project folder
    pwd
    ls
    # Initialize an empty Git repository
    git init
    ```

-   What happened?

-   Each time you want to use version control for a new project, you
    have first to create an empty repository with `git init`.

### Where does Git store its files?

-   Git stores all its information in the `.git` folder.

-   Folders and files whose name starts with a dot are hidden from the
    `ls` output by default, but you can force their display with:

    ``` {.bash}
    ls -a
    ```

-   You can combine `ls` options:

    ``` {.bash}
    ls -al
    ```

-   In `ls -al` output:
    -   the folder `.` is the current folder
    -   the folder `..` is the parent folder

3.2 Check current status, track and commit your changes
-------------------------------------------------------

-   We can always ask Git about the status of our current repository
    with `git
     status`. Try it:

    ``` {.bash}
    git status
    ```

-   Git doesn't know yet which file we want to track. The first step is
    to specify which changes we want to add to our repository. We use
    the `git add` command for that:

    ``` {.bash}
    git add pancakes
    ```

-   What is the status now?

    ``` {.bash}
    git status
    ```

-   Git has some changes ready to be saved (they are **staged**). To
    actually save them to the repository, we tell git to commit the
    staged changes:

    ``` {.bash}
    # Specify a commit message after the -m option
    git commit -m "Create a recipe for pancakes"
    ```

-   What happened?

### Tell Git who you are

-   One of the key feature of a version control system is to assign each
    change to someone. This ensures that all modifications can be traced
    to their original author.

-   The first time you use Git, you have to configure it with your name
    and your email address. You have to do this only once.

-   Configure Git with:

    ``` {.bash}
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    ```

### Back to the commit

-   Try again to commit:

    ``` {.bash}
    # Specify a commit message after the -m option
    git commit -m "Create a recipe for pancakes"
    ```

-   It is **very important** to use **concise and meaningful commit
    messages**!

-   What is the current status of the repository?

3.3 Commit more changes
-----------------------

-   Your list of ingredients is missing something. Update it:

    ``` {.example}
    Pancake recipe

    Ingredients:
     500g of flour
     5 (or 4) eggs
     1 liter of milk
     salt, oil
    ```

-   What is the status of the repository now?

-   Let's have a look at what actually change with `git diff`:

    ``` {.bash}
    git diff
    ```

-   `git diff` works by lines by default, but we can make it work by
    "words":

    ``` {.bash}
    git diff --word-diff
    ```

-   Let's commit our changes:

    ``` {.bash}
    git commit -m "Add missing ingredients for pancakes"
    ```

-   What happened?

### The staging area

-   Even if Git knows which files to track, by default it **does not**
    commit automatically all changes.

-   You have first to **stage** the changes by using `git add` again,
    and **then** to commit them with `git commit`:

    ``` {.bash}
    git add pancakes
    git commit -m "Add missing ingredients for pancakes"
    ```

-   This might look pretty inefficient, but it gives you more control
    and flexibility over what you want to commit exactly when you have
    several files which have been changed.

-   Often, however, you want to commit all the changes in the tracked
    files in one go. In this case, you can use the shortcut:

    ``` {.bash}
    git commit -a -m "Add missing ingredients for pancakes"
    # which is equivalent to
    git commit -am "Add missing ingredients for pancakes"
    ```

-   The `-a` option tells Git to automatically add all changes in
    tracked files for commit.

3.4 Explore history
-------------------

-   Your repository history can be explored with:

    ``` {.bash}
    git log
    ```

-   You can amend your last commit message with:

    ``` {.bash}
    git commit --amend -m "Add salt and oil for pancakes"
    # View history
    git log
    ```

-   You can have a look at the Git log of
    [ggplot2](https://github.com/tidyverse/ggplot2/commits/master) for
    an example of history for a large project.

### What we learnt about in this section

-   **Tracking** a file and **committing** changes
-   The **staging area** (and how to use the `-a` option)
-   **Amend** commit messages
-   Git **log** to explore project history

4 Git basics (2) - Commit hashes and revert to previous versions
================================================================

4.1 Write some recipe instructions
----------------------------------

-   Add some instructions about to make the pancake dough

-   If you are happy with your report, commit your changes:

    ``` {.bash}
    git status
    git diff
    git commit -am "Add preparation instruction for the pancake recipe"
    ```

-   Add more information about the cooking. Commit your changes.

-   Have a look at your history. Are your commit messages clear enough?

4.2 Diff
--------

-   You want to see what is the overall difference between your latest
    commit and the first commit you did.

-   You already know how to get the difference between the last commit
    and your current files with `git diff`. You can also use `git diff`
    to compare commits.

### A word about commit hash

-   Each commit is identified by a unique commit hash

    ``` {.example}
    commit d26f19ab15bf2baa9b2eaa42946689a4289546b0
    Author: Matthieu Bruneaux <matthieu.bruneaux@gmail.com>
    Date:   Thu Nov 10 14:11:21 2016 +0200

        Basics for committing

    commit 9119038c82837229fccb44e9e309d0c307b4a6c3
    Author: Matthieu Bruneaux <matthieu.bruneaux@gmail.com>
    Date:   Thu Nov 10 14:11:01 2016 +0200

        Add note about no copy-paste

    ```

-   These commit hashes can be used to specify which commits to compare
    with `git diff`:

    ``` {.bash}
    git diff 9119038c82837229fccb44e9e309d0c307b4a6c3 d26f19ab15bf2baa9b2eaa42946689a4289546b0
    ```

-   However, you don't need to always type the full hash. Often, the
    first characters are enough:

    ``` {.bash}
    git diff 9119038 d26f19a
    ```

### Do the `diff`

-   Use `git diff` and commit hashes to compare your first and your
    last commits.

-   What about comparing your first and your second commit?

4.3 Revert
----------

-   Add some ingredients so that your pancake becomes a Hawaiian
    pancake:

        Pancake recipe

        Ingredients:
         500g of flour
         5 (or 4) eggs
         1 liter of milk
         salt, oil
         pineapple juice
         coconut syrup

-   Commit your changes.

-   Unfortunately, you heard that the National Finnish Institute for
    Pancakes emitted an official recommendation against pineapple in
    pancake dough. We have to revert to the previous version.

-   To revert to a previous version, observe the hash of the version you
    want to revert to in Git history, and type:

        git checkout f32a121

-   Commit your changes.

What we learnt about in this section
------------------------------------

-   Use **diff** to compare files
-   Commits are identified by unique **hashes**
-   How to **revert** to a previous version with `git checkout`

5 Intermediate (1) - Branching and merging
==========================================

-   You think about adding a Christmas section to your book. You want to
    start working in this direction, but you are not totally sure you
    will end up using this version.

-   Let's create a new branch for our work:

        git branch christmas
        git checkout christmas

-   We are now working in the `christmas` branch. Everything we do here
    will not have any effect on the `master` branch, which will
    remain clean.

-   Run `git status`. What do you observe?

-   Run `git log`. What do you observe?

-   Modify the recipe in `pancakes`:

        Pancake recipe

        Ingredients:
         500g of flour
         5 (or 4) eggs
         0.5 liter of milk
         0.5 liter of Glögi
         salt, oil
         cinnamon

-   Create a new recipe in a file called `snails`:

        Snails recipe

        Ingredients:
         Burgundy snails
         lots of garlic butter

-   Commit both the changes to `pancakes` and the new file `snails`

-   Have a look to your repository history

-   Switch back to the master branch with:

        git checkout master

-   Have a look at your folder content and at `pancakes`.

-   You now think that this Christmas project is a good thing and want
    to merge it with your master branch:

        git merge christmas

-   Have a look at your repository history.

6 Intermediate (2) - Cloning a remote repository
================================================

-   Repositories can easily be shared between collaborators, published
    online and copied locally from a remote location.

-   Copying a remote repository to your computer is called **cloning**.

6.1 Find an interesting repository to clone on GitHub
-----------------------------------------------------

-   Go to [GitHub](https://github.com/), a platform to
    host repositories.

-   Search for a repository of interest you might want to copy to
    your computer. In this example, we will clone the **recipes**
    repository from Hadley Wickham ([GitHub
    repo](https://github.com/hadley/recipes)).

-   Go back to your home folder with `cd`

-   Clone the repository of your choice locally with:

    ``` {.bash}
    git clone https://github.com/hadley/recipes.git
    # Replace the repository address appropriately
    ```

6.2 Explore the repository locally
----------------------------------

-   Now cd into the cloned repository

-   Explore the history and commits of the repository. What were the
    changes in the last commit? Who did it? Are there several
    contributors?

-   Did the author(s) use any branches?

-   Any interesting commit message?

-   Any interesting branching structure?

-   Modify one of the files and commit your changes

-   Have a look at the history and feel proud.

-   Remember: your commit messages should be clear and to the point!

*images/xkcd\_git\_commit.png*

([original link](https://xkcd.com/1296/))

7. Advanced - Setting up a remote repository
============================================

-   You are pretty proud of your python code to analyse coding sequences
    and want to do good to the world: let's share it publicly!

-   Let's use GitHub to host a public repository of your code.

7.1 Create a GitHub account
---------------------------

-   We are going to create a GitHub repository for you (you can use a
    pseudonyme and delete the account afterwards if you don't want to
    give GitHub your real information)

\*Note\*: you **don't have to** create a GitHub account if you don't
want to - we totally understand you might be concerned about creating
yet-another-account on a remote service. So please **don't feel obliged
to do so**, and if you prefer not to do it just find a bootcamp partner
who has a GitHub account to follow the next session with him/her.

-   Go to [GitHub](https://github.com/) and create an account.

-   If you are creating a temporary account, don't forget to delete it
    after the course in order to clean things up on GitHub.

-   Login to your GitHub account.

-   Create a new repository for your small Python project.

7.2 Adding a remote to your local repository
--------------------------------------------

-   Go back to your project directory where you wrote the Python code.

-   Add a remote to your repository with:

    ``` {.bash}
    git remote add origin git@github.com:myusername/myrepo.git
    # Use the appropriate address
    ```

    -   `git remote`: command to manage remote repositories
    -   `add`: we create a new link between our local repo and a remote
        server
    -   `origin`: this new link is called `origin` for ease of use
    -   `git@github.com:....`: this is the address of the remote
        repository
-   You are ready to push your local repository to the GitHub server:

    ``` {.bash}
    git push origin master
    ```

    -   `git push`: command to push the local repository data to remote
        servers
    -   `origin`: the name of the link to a remote server we want to use
        (defined when we created the remote link with
        `git remote add ...`)
    -   `master`: the branch we want to push. For now we have only been
        working with a single, master branch called `master` by default
-   Have a look to your repository on GitHub now. How does it look like?

7.3 Pushing local changes to a remote server
--------------------------------------------

-   Create a README file in your project folder, fill it with
    interesting information and commit it to your repository.

-   Push your changes to the remote repository:

    ``` {.bash}
    git push
    ```

-   Have a look to the remote repository on GitHub (you might need to
    refresh the browser page)

8. Advanced - Collaborative work
================================

TODO merge conflicts

In this last section, we are going to clone the remote repository you
just made to your own computer and create branches. Branches will allow
you to write exploratory code which you are not sure you want to put in
the master branch of your project yet.

### 3.3.1 Clone your own repository to your machine

-   Now we will log out from the **bio109-113** server and work on your
    truly local machine.

-   Create a local folder for the practicals and clone the repository
    which was put on GitHub locally:
    -   If you are using Windows, you can use `git bash`
    -   If you are using GNU/Linux or a Mac, you can use `git` from a
        terminal

### 3.3.2 Write some code

-   Now you are ready for some serious analysis. You think that
    **histidine** is a particularly interesting amino-acid, and you
    would like to count how many histidine-coding triplets you have per
    coding sequence. However, this is a quite experimental part of your
    analysis: create a new branch, add your function and test it. When
    you are satisfied with it, merge it to your master branch.
-   Actually, it would be nice if your function could count **any**
    codons, not just histidine-coding ones. This is even more
    experimental, so create another branch, modify your function, and...
-   Wait, your supervisor asks you to add as quickly as possible a
    checking step so that only A, T, G, C are allowed in the sequences.
    This is a crucial update, so do it in your master branch and commit.
-   Now you can go back to your experimental branch. Finish your
    function modification, test it and merge it with your master branch
    when you are happy.
-   Resolve merging conflicts as they arise.

Going further: workflow example for single developper
=====================================================

Resources
=========

links go here

Notes
=====

Exercise: design a set of Python scripts to handle fasta sequences

Coding sequences, check for beginning of ORF, stop-codon, translation,
etc...

Load the translation table from a text file

Track and fix errors in this file

Testing with this file

Profiling: translation with list vs dictionary

What is version-controlled? Scripts, not data, except if hand-generated
data (e.g. transcription of written records)
