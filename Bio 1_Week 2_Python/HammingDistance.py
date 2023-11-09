def hamming_distance(gene1, gene2):
    if len(gene1) != len(gene2):
        raise ValueError("Genes must have the same length")

    distance = 0
    for char1, char2 in zip(gene1, gene2):
        if char1 != char2:
            distance += 1

    return distance


# Example usage:
gene1 = "GAGG"
gene2 = "AGGG"
distance = hamming_distance(gene1, gene2)
print(f"Hamming distance between gene1 and gene2: {distance}")
