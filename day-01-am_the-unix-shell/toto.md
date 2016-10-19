Before the course
-----------------

Prerequisites:
-   you have used a computer before and you are know what are "files"
    and "directories" or "folders" on a computer

After the course
----------------

You will know how to:
-   connect to a remote server
-   navigate around files and folders from the command line
-   create, copy, move and delete files and folders
-   run programs from the command line
-   combine commands to perform complex operations
-   create scripts to automate task

What is the shell?
==================

![](images/shell-screenshot.png)

In brief:
-   Command-line interface, looks old-fashioned but very convenient
-   Main interface when you want to login to **remote servers** (e.g.
    CSC servers)
-   Also present in **Linux** distributions for personal computers and
    **Macs**
-   With **Windows**, the `cmd` prompt is a bit similar (text-based) but
    not as powerful

Usage:
-   Often the only interface for remote connections
-   Powerful built-in commands
-   **Automate repetitive tasks**
-   Shell scripts to **reproduce** data manipulation

Where can we find the shell?
============================

To find a shell:
-   On **GNU/Linux** and **MacOS** systems: open a **terminal**. This
    will provide you with a Unix-like shell on both systems.
-   On **Windows**: run `cmd.exe` or `cmd`. This shell is quite
    different from the Unix-like shell found in Linux and MacOS. To
    obtain a Unix shell on Windows, one caninstall the Cygwin tools.
-   It is strongly recommended to learn how to use a **Unix shell**
    since it is very likely it is this type of shell you will be exposed
    to when you connect to a **remote server**.

One shell or several shells?
----------------------------

-   A shell: a program providing an **interface** between the user and
    the computer. **Different shells exist**.
-   The most popular ad widely used shell is probably **bash**. It is
    the default shell in most GNU/Linux distributions.
-   If you learn how to use **bash**, you will be able to use most
    **remote servers** you'll have to connect to, and also the
    **terminal** from MacOS or the **Cygwin** tools on Windows.

\*One word on terminology:\* During the course, we will often say
interchangeably "the terminal", "the console", "the shell" or "bash".

The CSC center in Kajaani
=========================

![](images/digitice-csc-kajaani-800_ilmakuva_tehtaasta.jpg)

Meet the Taito cluster (`taito.csc.fi`)
=======================================

![](images/yle-taito-supertietokone-kajaani.jpg)

A word about CSC servers
========================

Available servers:
-   **Taito:** 19152 cores (16 cores per node)
-   **Sisu:** 39408 cores, for massively parallel jobs

Job submission:
-   CPU-intense calculations have to be submitted through a queue system
-   Server load and CPU quota
-   We can also run some simple commands directly at login

Module system:
-   Many softwares installed
-   Sometimes different versions of a given software
-   User has to explicitly load **modules**

Hands-on practice
=================

1. Connection to a remote shell
-------------------------------

The plan:
-   Using the CSC server Taito in Kaajani (student account)
-   Tools: **putty** (Windows) or **ssh** (Mac and GNU/Linux)
-   A word about **ssh** and the **security of connections**?

Student account:
-   Logins: `jyybio01` to `jyybio02`
-   Password: on the whiteboard

Connection:
-   From a terminal (Mac or GNU/Linux):

    ``` {.bash}
    ssh jyybioxx@taito.csc.fi
    ```

    where `xx` is your student number.
-   From Putty: ask a teacher if needed

2. First contact with the shell
-------------------------------

### 2.1 Just after connection:

-   What you see after connection is the **shell prompt**. It tells you
    the shell is ready to receive your input:

    ``` {.example}
    jyybioxx@taito-login3$
    ```

-   `jyybioxx` is your username, `taito-login` is the host server to
    which you are connected. The number after `taito-login` can vary
    because Taito has several login nodes.

### 2.2 Execute a command (`ls`)

-   The shell **reads** and **executes** commands you enter at the
    prompt, and **prints** the output.
-   Type:

    ``` {.bash}
    ls
    ```

    and press `RETURN`. You should see:

    ``` {.example}
    appl_taito
    ```

-   You just ran the `ls` command which produces an output: the list of
    files and folders present in the current directory.
-   Try another command:

    ``` {.bash}
    whoami
    ```

    What does this command do?

### 2.3 Execute a command (`pwd`)

-   When you login to a server, you are automatically sent to your
    home folder.
-   You can see where you are by typing:

    ``` {.bash}
    pwd
    ```

    which produces:

    ``` {.example}
    /homeappl/home/jyybioxx
    ```

-   So you are now in the folder `jyybioxx`, which is itself contained
    in `home`, which is contained in `homeappl`, which is at the root of
    the file system (`/`, there is no parent directory above).

