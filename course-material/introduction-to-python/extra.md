# End of the course: complete script

* Write a script which loads some aligned fasta sequences from a file and plot
  the residue conservation along the primary sequence
* This script can be used as an example material for the version control course

## Requirements
* numpy
* matplotlib
* python-Levenshtein
* biopython

## Method
* Read fasta file with sequences and store first sequence as `base_sequence`.
* Compare all other sequences using levenshein distances.
* convert length list to numpy array
* pyplot.plot to see graph of data
* pyplot.hist to plot a histogram
