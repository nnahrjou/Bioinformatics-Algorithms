def hamming_distance(gene1, gene2):
    if len(gene1) != len(gene2):
        raise ValueError("Genes must have the same length")

    distance = 0
    for char1, char2 in zip(gene1, gene2):
        if char1 != char2:
            distance += 1

    return distance


# Example usage:
# gene1 = "AGTACGTACA"
# gene2 = "AGTCCGTAGT"
# distance = hamming_distance(gene1, gene2)
# print(f"Hamming distance between gene1 and gene2: {distance}")


# def ImmediateNeighbors(Pattern):
#     Neighborhood = set()  # Set to store the immediate neighbors

#     # Add the original pattern to the neighborhood
#     Neighborhood.add(Pattern)

#     # Loop through each position in the pattern
#     for i in range(len(Pattern)):
#         symbol = Pattern[i]  # Get the i-th nucleotide

#         # Loop through each possible nucleotide different from the current symbol
#         for x in 'ACGT':
#             if x != symbol:
#                 # Generate a neighbor by substituting the i-th nucleotide with x
#                 Neighbor = Pattern[:i] + x + Pattern[i+1:]
#                 Neighborhood.add(Neighbor)

#     return Neighborhood


# Example usage:
# Pattern = "ACGT"
# result = ImmediateNeighbors(Pattern)
# print(result)


# def hamming_distance(gene1, gene2):
#     # Assuming HammingDistance is defined and calculates the Hamming distance between two strings
#     pass


def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    Neighborhood = set()  # Set to store the neighbors

    # Recursively find neighbors for the suffix of Pattern
    SuffixNeighbors = Neighbors(Pattern[1:], d)

    for Text in SuffixNeighbors:
        if hamming_distance(Pattern[1:], Text) < d:
            for x in 'ACGT':
                Neighborhood.add(x + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)

    return Neighborhood


# Example usage:
Pattern = "ACGT"
d = 3
result = Neighbors(Pattern, d)
print(result)
