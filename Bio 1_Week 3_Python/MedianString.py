def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings of equal length."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def d(pattern, dna):
    """Calculate the total Hamming distance between the pattern and all k-mers in DNA."""
    return sum(min(hamming_distance(pattern, kmer), len(pattern)) for kmer in dna)


def median_string(dna, k):
    distance = float('inf')
    median = ""

    nucleotides = ['A', 'C', 'G', 'T']

    # Generate all possible k-mers
    for i in range(4 ** k):
        pattern = ""
        index = i
        for _ in range(k):
            pattern = nucleotides[index % 4] + pattern
            index //= 4

        curr_distance = d(pattern, dna)

        if curr_distance < distance:
            distance = curr_distance
            median = pattern

    return median


# Example usage
k = 3
Dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

result = median_string(Dna, k)
print(result)
