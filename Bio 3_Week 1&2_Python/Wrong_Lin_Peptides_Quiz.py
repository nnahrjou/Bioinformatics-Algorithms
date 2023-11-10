def count_peptides(target_mass, amino_acids):
    # Create a memoization table to store previously calculated values
    memo = [0] * (target_mass + 1)
    memo[0] = 1

    # Iterate through the amino acids and update the memo table
    for amino_acid in amino_acids:
        for i in range(amino_acid, target_mass + 1):
            memo[i] += memo[i - amino_acid]

    return memo[target_mass]


# Amino acids mass: X=2, Z=3
amino_acids_mass = {'X': 2, 'Z': 3}

# Target total mass
target_total_mass = 25

# Calculate the number of possible linear peptides
num_peptides = count_peptides(target_total_mass, amino_acids_mass.values())

print("Number of possible linear peptides:", num_peptides)
