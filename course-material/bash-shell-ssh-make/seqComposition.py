### * Description

# Script to determine the amino acid composition of peptide sequences
# in a fasta file
# Requires Python 3

### * Setup

### ** Import

import sys
import argparse

### ** Parameters

myAA = "ARNDCEQGHILKMFPSTWYVX"

### ** Argument parser

parser = argparse.ArgumentParser(description = "Script to determine the amino \
             acid composition of peptide sequences in a fasta file. Requires \
             Python 3")
parser.add_argument("input", metavar = "INPUT_FILE",
                    nargs = 1,
                    help = "Input file")

### * Functions

### ** parse_fasta(input_file)

def parse_fasta(input_file) :
    """ 
    TAKES
    input_file: string, path to the input file
    RETURNS
    An iterator producing tuples (seqName, sequence)
    """
    with open(input_file, "r") as fi :
        seqName = ""
        sequence = ""
        for l in fi :
            l = l.strip()
            if l.startswith(">") :
                if seqName != "" and sequence != "" :
                    yield (seqName, sequence)
                seqName = l[1:]
                sequence = ""
            else :
                sequence += l
        if seqName != "" and sequence != "" :
            yield (seqName, sequence)

### ** aaComposition(sequence)

def aaComposition(sequence) :
    """
    TAKES
    sequence: string containing an amino-acid sequence in one-letter code
    RETURNS
    A dictionary with the count for each letter
    """
    o = dict()
    for aa in myAA :
        o[aa] = sequence.count(aa)
    assert sum(o.values()) == len(sequence)
    return(o)

### * Run

if (__name__ == "__main__") :
    args = parser.parse_args()

### ** Go through the input file

seqs = parse_fasta(args.input[0])
headers = "\t".join(myAA) + "\tname"
print(headers)
for seq in seqs :
    print("\t".join([str(aaComposition(seq[1])[x]) for x in myAA]) + "\t" + seq[0])
