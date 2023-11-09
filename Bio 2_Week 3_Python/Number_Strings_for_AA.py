# Codons for each amino acid
codons = {
    'C': ['TGT', 'TGC'],
    'Y': ['TAT', 'TAC'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'I': ['ATT', 'ATC', 'ATA'],
}

# Count the number of possible DNA sequences for each amino acid
num_sequences = [len(codons[aa]) for aa in "CYCLIC"]

# Calculate the total number of possible DNA sequences
total_sequences = 1
for count in num_sequences:
    total_sequences *= count

print("Total number of DNA sequences:", total_sequences)
