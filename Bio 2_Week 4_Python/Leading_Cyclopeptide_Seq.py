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

# Function to calculate the score of a peptide against a spectrum
def score(peptide, spectrum):
    theoretical_spec = theoretical_spectrum(peptide)
    score = 0
    for mass in spectrum:
        if mass in theoretical_spec:
            score += 1
            theoretical_spec.remove(mass)
    return score

# Function to expand the leaderboard
def expand(leaderboard):
    new_leaderboard = []
    for peptide in leaderboard:
        for amino_acid in "GASPVTCILNDKEMHFRYW":
            new_leaderboard.append(peptide + amino_acid)
    return new_leaderboard

# Function to trim the leaderboard
def trim(leaderboard, spectrum, N):
    scores = [(peptide, score(peptide, spectrum)) for peptide in leaderboard]
    scores.sort(key=lambda x: x[1], reverse=True)
    trimmed = [peptide for peptide, _ in scores[:N]]
    return trimmed

# LeaderboardCyclopeptideSequencing algorithm
def leaderboard_cyclopeptide_sequencing(spectrum, N):
    leaderboard = [""]
    leader_peptide = ""
    parent_mass = max(spectrum)
    
    while leaderboard:
        leaderboard = expand(leaderboard)
        for peptide in leaderboard.copy():
            if mass(peptide) == parent_mass:
                if score(peptide, spectrum) > score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif mass(peptide) > parent_mass:
                leaderboard.remove(peptide)
        leaderboard = trim(leaderboard, spectrum, N)
    
    return leader_peptide

# Sample input
spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
N = 10

# Run the algorithm and print the result
result = leaderboard_cyclopeptide_sequencing(spectrum, N)
print(result)
