def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings of equal length."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0

    for text in dna:
        hamming_distance_min = float('inf')
        for i in range(len(text) - k + 1):
            kmer = text[i:i + k]
            hamming_dist = hamming_distance(pattern, kmer)
            if hamming_dist < hamming_distance_min:
                hamming_distance_min = hamming_dist
        distance += hamming_distance_min

    return distance


# Example usage
pattern = "AAA"
dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

result = distance_between_pattern_and_strings(pattern, dna)
print(result)
