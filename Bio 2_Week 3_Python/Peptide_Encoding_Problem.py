from collections import Counter
from structures import *


Nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


# def validateSeq(dna_seq):
#     tmpseq = dna_seq.upper()
#     for nuc in tmpseq:
#         if nuc not in Nucleotides:
#             return False
#     return tmpseq
# # Check the sequence to make sure it is a valid DNA string


def peptide_encoding_problem(dna, peptide):
    sequence = []
    protein_length = len(peptide)
    for i in range(len(dna) - 3 * protein_length + 1):
        if protein_translation(dna_rna(dna[i:i + protein_length * 3])) == peptide \
                or protein_translation(dna_rna(reverse_complement(dna[i:i + protein_length * 3]))) == peptide:
            sequence.append(dna[i:i + protein_length * 3])
    return sequence


def protein_translation(rna):
    protein = ""
    for i in range(0, len(rna), 3):
        if rna_codons[rna[i:i + 3]]:
            protein += rna_codons[rna[i:i + 3]]
        else:
            return protein
    return protein


def dna_rna(dna):
    return dna.replace('T', 'U')


def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")


def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


if __name__ == '__main__':
    data = "".join(open('peptide_encoding_problem.txt')).split()
    # print(data)
    rna_codons = dict()
    with open('genetic_code.txt') as f:
        for i in f:
            i = i.split()
            if len(i) > 1:
                rna_codons[i[0]] = i[1]
            else:
                rna_codons[i[0]] = []
    # print(rna_codons)
    for i in peptide_encoding_problem(data[0], data[1]):
        print(i)