def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings of equal length."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def generate_neighbors(pattern, d):
    """Generate all k-mers within Hamming distance d from the given pattern."""
    if d == 0:
        return [pattern]

    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighborhood = set()
    suffix_neighbors = generate_neighbors(pattern[1:], d)

    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)

    return list(neighborhood)


def motif_enumeration(Dna, k, d):
    Patterns = set()

    for dna_string in Dna:
        for i in range(len(dna_string) - k + 1):
            pattern = dna_string[i:i + k]
            neighbors = generate_neighbors(pattern, d)

            for neighbor in neighbors:
                if all(any(hamming_distance(neighbor, seq[j:j + k]) <= d for j in range(len(seq) - k + 1)) for seq in Dna):
                    Patterns.add(neighbor)

    return list(Patterns)


# Example usage
k = 5
d = 2
Dna = ["CATAACTGTTTCGGCTGCAGAACCT", "TTCAGAAGATTGCTCACATATGCGT", "ATCTGATTCAAGCGATGCACCTGAG",
       "CGGTTTGCCTGGAATGGAGGTGGAG", "ACTATCTCAAATCCGTGCAGGACTA", "TAGTTAGGAGAGACTCTCCTTGCCG"]
result = motif_enumeration(Dna, k, d)
print(result)
