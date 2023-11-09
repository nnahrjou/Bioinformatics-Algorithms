# Function to compute the linear score of a peptide against a spectrum
def linear_score(peptide, alphabet, amino_acid_mass, spectrum):
    theoretical_spec = theoretical_spectrum(peptide, alphabet, amino_acid_mass)
    score = 0
    for mass in spectrum:
        if mass in theoretical_spec:
            score += 1
            theoretical_spec.remove(mass)
    return score

# Function to calculate the theoretical spectrum of a peptide
def theoretical_spectrum(peptide, alphabet, amino_acid_mass):
    spectrum = [0]
    for length in range(1, len(peptide) + 1):
        for i in range(len(peptide) - length + 1):
            sub_peptide = peptide[i:i+length]
            mass = sum(map(lambda aa: amino_acid_mass[aa], sub_peptide))
            spectrum.append(mass)
    spectrum.sort()
    return spectrum

# Function to implement the Trim function
def trim_leaderboard(leaderboard, spectrum, N, alphabet, amino_acid_mass):
    linear_scores = []
    for peptide in leaderboard:
        score = linear_score(peptide, alphabet, amino_acid_mass, spectrum)
        linear_scores.append(score)
    
    # Sort Leaderboard and LinearScores
    leaderboard_scores = list(zip(leaderboard, linear_scores))
    leaderboard_scores.sort(key=lambda x: x[1], reverse=True)
    leaderboard, linear_scores = zip(*leaderboard_scores)
    
    # Trim the leaderboard
    for j in range(N, len(leaderboard)):
        if linear_scores[j] < linear_scores[N - 1]:
            return leaderboard[:j]
    
    return leaderboard

# Sample input
leaderboard = ["LAST", "ALST", "TLLT", "TQAS"]
spectrum = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
N = 2
alphabet = "ACDEFGHIKLMNPQRSTVWY"
amino_acid_mass = {
    'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 'G': 57,
    'H': 137, 'I': 113, 'K': 128, 'L': 113, 'M': 131, 'N': 114,
    'P': 97, 'Q': 128, 'R': 156, 'S': 87, 'T': 101, 'V': 99,
    'W': 186, 'Y': 163
}

# Trim the leaderboard and print the result
result = trim_leaderboard(leaderboard, spectrum, N, alphabet, amino_acid_mass)
print(result)
