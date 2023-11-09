# Dictionary containing integer masses of amino acids
amino_acid_masses = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
    'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

def generate_subpeptides(peptide):
    subpeptides = [""]
    peptide_length = len(peptide)
    for length in range(1, peptide_length):
        for i in range(peptide_length - length + 1):
            subpeptide = peptide[i:i + length]
            subpeptides.append(subpeptide)
    subpeptides.append(peptide)
    return subpeptides

def calculate_linearspectrum(peptide):
    subpeptides = generate_subpeptides(peptide)
    spectrum = [0]
    for subpeptide in subpeptides:
        mass = sum(amino_acid_masses[aa] for aa in subpeptide)
        spectrum.append(mass)
    return sorted(spectrum)

if __name__ == '__main__':
    peptide = "TCE"
    spectrum = calculate_linearspectrum(peptide)
    print(" ".join(map(str, spectrum)))
