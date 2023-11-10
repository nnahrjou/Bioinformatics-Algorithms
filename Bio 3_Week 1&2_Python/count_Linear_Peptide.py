def count_linear_peptides(mass, current_sequence=""):
    if mass == 0:
        print(current_sequence)
        return 1

    total_count = 0

    if mass >= 2:
        total_count += count_linear_peptides(mass - 2, current_sequence + "X")

    if mass >= 3:
        total_count += count_linear_peptides(mass - 3, current_sequence + "Z")

    return total_count


total_peptides = count_linear_peptides(21)
print("Total number of possible linear peptides:", total_peptides)
