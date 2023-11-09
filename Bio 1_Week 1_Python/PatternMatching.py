def PatternMatching(Pattern, Genome):
    positions = []  # To store the starting positions of occurrences

    # Loop through the Genome string to find occurrences of the Pattern
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            positions.append(i)

    return positions


# Example usage:
Pattern = "AA"
Genome = "AAAAAAA"

result = PatternMatching(Pattern, Genome)
print(" ".join(map(str, result)))
