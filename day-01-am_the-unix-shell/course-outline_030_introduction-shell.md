Title: Introduction to the shell
Date: 2014-10-16
Summary: Description of the shell introductory course
Status: hidden

# Presentation of the shell

- Command line interface, looks old-fashioned but very convenient
- Main interface when you want to login to CSC servers or remote Linux servers
- Also present in Linux distributions for personal computers and Mac
- With Windows, the cmd prompt is a bit similar (text-based) but not as
  powerful

# Connection to a remote shell

- Connection to taito server
- Connection to linux.utu.fi
- Connection to desktop computer in Utu (if running Linux)
- Tools: putty (windows) or ssh (mac and linux)
- A word about the security of connections?

# Shell basics

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

# Shell scripts

-   Storing simple commands in shell scripts
-   Parsing arguments
-   Control flow (loops, if, while)
-   Applying script to all files in a directory
-   Version control of shell scripts
