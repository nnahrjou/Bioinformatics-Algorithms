def find_min_skew_position(sequence):
    skew_values = [0]  # Start with skew value of 0 at position 0

    # Calculate skew values for each position in the sequence
    for i, nucleotide in enumerate(sequence):
        if nucleotide == "G":
            skew_values.append(skew_values[i] + 1)
        elif nucleotide == "C":
            skew_values.append(skew_values[i] - 1)
        else:
            skew_values.append(skew_values[i])

    min_skew = min(skew_values)
    min_skew_positions = [i for i, skew in enumerate(
        skew_values) if skew == min_skew]

    return min_skew_positions


# Example sequence
sequence = "CATTCCAGTACTTCGATGATGGCGTGAAGA"

min_skew_positions = find_min_skew_position(sequence)
print("Positions with minimum skew:", min_skew_positions)
