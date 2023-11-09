import math


def calculate_motifs_entropy(motifs):
    k = len(motifs[0])
    counts = {'A': [0] * k, 'C': [0] * k, 'G': [0] * k, 'T': [0] * k}

    for i in range(k):
        for motif in motifs:
            counts[motif[i]][i] += 1

    entropy = 0.0
    for i in range(k):
        total_count = sum(counts[nucleotide][i] for nucleotide in counts)
        if total_count > 0:
            for nucleotide in counts:
                prob = counts[nucleotide][i] / total_count
                if prob > 0:
                    entropy -= prob * math.log2(prob)

    return entropy


# Example usage
motifs = ["CGC", "GAG", "TAA", "TGA", "TCC"]
entropy = calculate_motifs_entropy(motifs)
print("Motifs Entropy:", entropy)
