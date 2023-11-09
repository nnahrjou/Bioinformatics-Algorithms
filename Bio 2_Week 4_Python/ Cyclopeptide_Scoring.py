# Function to calculate the mass of an amino acid
def get_mass(amino_acid):
    mass_table = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
        'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
        'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
    }
    return mass_table[amino_acid]

# Function to calculate the theoretical spectrum of a peptide
def theoretical_spectrum(peptide):
    spectrum = [0]
    for length in range(1, len(peptide) + 1):
        for i in range(len(peptide)):
            sub_peptide = peptide[i:i+length]
            mass = sum(map(get_mass, sub_peptide))
            spectrum.append(mass)
    spectrum.sort()
    return spectrum

# Function to calculate the score of a peptide against a spectrum
def score(peptide, spectrum):
    theoretical_spec = theoretical_spectrum(peptide)
    score = 0
    for mass in spectrum:
        if mass in theoretical_spec:
            score += 1
            theoretical_spec.remove(mass)
    return score

# Read input
peptide = input().strip()
spectrum = list(map(int, input().strip().split()))

# Calculate and print the score
result = score(peptide, spectrum)
print(result)
