from collections import Counter
from structures import *


Nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq
# Check the sequence to make sure it is a valid DNA string


# Count nucleotides in a given sequence.

# def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict

    """
    Count nucleotides in a given sequence.
    Return a dictionary
    """
    # More Pythonic, using Counter
    # # import collections
    # return dict(collections.Counter(seq))


def countNucFrequency(seq):

    return dict(Counter(seq))


def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T",  "U")


def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    """
    Swapping adenine with thymine and guanine with cytosine.
    Reversing newly generated string
    """
    # if self.seq_type == "DNA":
    #     mapping = str.maketrans('ATCG', 'TAGC')
    # else:
    #     mapping = str.maketrans('AUCG', 'UAGC')
    # return self.seq.translate(mapping)[::-1]



def gc_content(seq):
        """GC Content in a DNA/RNA sequence"""
        return round((seq.count('C') + seq.count('G')) / len(seq) * 100)



def gc_content_subsec(seq, k=20):
        """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
        res = []
        for i in range(0, len(seq) - k + 1, k):
            subseq = seq[i:i + k]
            res.append(
                round((subseq.count('C') + subseq.count('G')) / len(subseq) * 100))
        return res