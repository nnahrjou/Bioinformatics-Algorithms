def max_skew_position(sequence):
    max_skew = 0
    max_positions = []

    skew = 0
    for i, nucleotide in enumerate(sequence):
        if nucleotide == "G":
            skew += 1
        elif nucleotide == "C":
            skew -= 1

        if skew > max_skew:
            max_skew = skew
            max_positions = [i + 1]  # Adding 1 to adjust for 1-based indexing
        elif skew == max_skew:
            max_positions.append(i + 1)

    return max_positions


# Example sequence
sequence = "CATTCCAGTACTTCATGATGGCGTGAAGA"

max_positions = max_skew_position(sequence)
print("Positions with maximum skew:", max_positions)
