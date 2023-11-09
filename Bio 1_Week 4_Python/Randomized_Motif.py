# There is sth wrong in this code!!!!

import random


def profile(motifs):
    k = len(motifs[0])
    profile_matrix = {'A': [0] * k, 'C': [0] * k, 'G': [0] * k, 'T': [0] * k}

    for i in range(k):
        for motif in motifs:
            profile_matrix[motif[i]][i] += 1

    for nucleotide in profile_matrix:
        for i in range(k):
            profile_matrix[nucleotide][i] /= len(motifs)

    return profile_matrix


def motifs(profile, dna):
    k = len(profile['A'])
    new_motifs = []

    for sequence in dna:
        most_probable = ""
        max_prob = 0.0
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i+k]
            prob = 1.0
            for j, nucleotide in enumerate(kmer):
                prob *= profile[nucleotide][j]
            if prob > max_prob:
                max_prob = prob
                most_probable = kmer
        new_motifs.append(most_probable)

    return new_motifs


def score(motifs):
    k = len(motifs[0])
    total_score = 0

    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        max_count = max(count.values())
        total_score += len(motifs) - max_count

    return total_score


def randomized_motif_search(dna, k, t):
    # Initialize with the first k-mers of each sequence
    best_motifs = [seq[:k] for seq in dna]

    while True:
        profile_matrix = profile(best_motifs)
        current_motifs = motifs(profile_matrix, dna)

        if score(current_motifs) < score(best_motifs):
            best_motifs = current_motifs
        else:
            return best_motifs


# Example usage
Dna = ["AAGCCAAA",
       "AATCCTGG",
       "GCTACTTG",
       "ATGTTTTG"]
k = 3
t = len(Dna)  # Set t to the number of sequences

best_motifs = randomized_motif_search(Dna, k, t)
print(best_motifs)
