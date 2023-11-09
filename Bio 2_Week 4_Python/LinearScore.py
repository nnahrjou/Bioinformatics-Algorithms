# Function to calculate the mass of an amino acid
def get_mass(amino_acid):
    mass_table = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
    }
    return mass_table[amino_acid]

# Function to calculate the mass of a peptide
def mass(peptide):
    return sum(map(get_mass, peptide))

# Function to calculate the theoretical spectrum of a peptide
def theoretical_spectrum(peptide):
    spectrum = [0]
    for length in range(1, len(peptide) + 1):
        for i in range(len(peptide)):
            sub_peptide = peptide[i:i+length]
            spectrum.append(mass(sub_peptide))
    spectrum.sort()
    return spectrum

# Function to calculate the linear score of a peptide against a spectrum
def linear_score(peptide, spectrum):
    theoretical_spec = theoretical_spectrum(peptide)
    score = 0
    for mass in spectrum:
        if mass in theoretical_spec:
            score += 1
            theoretical_spec.remove(mass)
    return score

# Read input from a file
with open("LinearScore_111.txt", "r") as f:
    peptide = f.readline().strip()
    spectrum = list(map(int, f.readline().strip().split()))

# Calculate the linear score
result = linear_score(peptide, spectrum)

# Print the result
print(result)
