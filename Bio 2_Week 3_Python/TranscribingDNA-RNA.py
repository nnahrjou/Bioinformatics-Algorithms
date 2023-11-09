Nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T",  "U")


print(transcription("CCACGTACTGAAATTAAC"))
