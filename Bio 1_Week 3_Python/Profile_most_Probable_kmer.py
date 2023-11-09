def profile_most_probable_kmer(text, k, profile):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    max_prob = -1
    most_probable = ""

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1.0

        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotides[nucleotide]][j]

        if prob > max_prob:
            max_prob = prob
            most_probable = kmer

    return most_probable


# Example usage
text = "AAGTTC"
k = 6
profile = [
    [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
]

result = profile_most_probable_kmer(text, k, profile)
print(result)
