# Introduction to the shell and task automation

(Matthieu Bruneaux)

## Presentation of the shell

- Command line interface, looks old-fashioned but very convenient
- Main interface when you want to login to CSC servers or remote Linux servers
- Also present in Linux distributions for personal computers and Mac
- With Windows, the cmd prompt is a bit similar (text-based) but not as
  powerful

## Where can we find the shell?

- On Linux and MacOS systems: open a terminal. This will provide you with a
  Unix-like shell on both systems
- On Windows: run "cmd.exe" or "cmd". This shell is quite different from the
  Unix-like shell found in Linux and MacOS. To obtain a Unix shell on
  Windows, one can install the [Cygwin](https://www.cygwin.com/) tools
- It is strongly recommended to learn how to use a Unix shell since it is very
  likely it is this type of shell you will be exposed to when you connect to a
  remote server.

## One shell or several shells?

- A shell is a just a program providing an interface between the user and the
  computer. Several different programs (shells) exist that can fulfill this
  task.
- The most popular and widely used shell is probably **bash**. It is the
  default shell in most GNU/Linux distributions.
- If you learn how to use **bash**, you will be able to use most remote servers
  you'll have to connect to, and also the terminal from MacOS or the Cygwin
  tools on Windows

## Connection to a remote shell

- Connection to taito server using the provided student accounts and password
- Connection to linux.utu.fi
- Connection to desktop computer in Utu (if running Linux)
- Tools: putty (windows) or ssh (mac and linux)
- A word about the security of connections?

## Shell basics

- Different flavours of shell (bash, tcsh, &#x2026;)
- Files and directories (ls, rm, mv, cp, mkdir, touch)
- Owners, groups and rwx rights
- Reading files (cat, less)
- Redirection (>, >>, <)
- stdin, stdout, stderr
- grep, wc, sort, uniq, cut, sed
- pipes
- example of a pipe to process a data file (count number of different species
in aligned sequences in a fasta files: grep for ">", cut for species name, sort
and uniq, wc)
- shell cheat sheet (Tiina prepared one for the Jyväskylä workshop in 2011)

### First contact with the shell

- What you see after connection in the **shell prompt**. It tells you the shell
is ready to receive your input:

    jyybio20@taito-login3$

`jyybio20` is your username, `taito-login` is the host server to which you are
connected.



## Shell scripts

-   Storing simple commands in shell scripts
-   Parsing arguments
-   Control flow (loops, if, while)
-   Applying script to all files in a directory
-   Version control of shell scripts
