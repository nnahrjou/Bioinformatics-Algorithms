from DNAToolkit import *
from utilities import colored
import random


# Creating a random DNA sequence for testing:

rndDNAStr = "ATTTCG"

# randDNAStr = ''.join([random.choice(Nucleotides)
#                      for nuc in range(50)])


DNAStr = validateSeq(rndDNAStr)
# print(validateSeq(randDNAStr))
# print(countNucFrequency(DNAStr))
# print(transcription(DNAStr))


print(f'\nSequence: {(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print((f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print(f'[3] + DNA/RNA Transcription: {(transcription(DNAStr))}\n')

# print(reverse_complement(DNAStr))

print(
    f"[4] + DNA String + Complement + Reverse Complement:\n5' {DNAStr} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {(reverse_complement(DNAStr))[::-1]} 5' [Complement]\n")
print(f"5' {(reverse_complement(DNAStr))} 3' [Rev. Complement]\n")


print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')

print(
    f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')
