import random


def profile(motifs):
    k = len(motifs[0])
    profile_matrix = {'A': [0] * k, 'C': [0] * k, 'G': [0] * k, 'T': [0] * k}

    for i in range(k):
        for motif in motifs:
            profile_matrix[motif[i]][i] += 1

    for nucleotide in profile_matrix:
        for i in range(k):
            profile_matrix[nucleotide][i] /= len(motifs)

    return profile_matrix


def find_motifs(profile, dna, i):
    k = len(profile['A'])
    new_motifs = []

    for idx, sequence in enumerate(dna):
        if idx == i:
            continue
        most_probable = ""
        max_prob = 0.0
        for j in range(len(sequence) - k + 1):
            kmer = sequence[j:j+k]
            prob = 1.0
            for l, nucleotide in enumerate(kmer):
                prob *= profile[nucleotide][l]
            if prob > max_prob:
                max_prob = prob
                most_probable = kmer
        new_motifs.append(most_probable)

    return new_motifs


def score(motifs):
    k = len(motifs[0])
    total_score = 0

    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        max_count = max(count.values())
        total_score += len(motifs) - max_count

    return total_score


def gibbs_sampler(dna, k, t, N):
    current_motifs = [random.choice(
        [seq[i:i+k] for i in range(len(seq) - k + 1)]) for seq in dna]
    best_motifs = current_motifs.copy()

    for _ in range(N):
        i = random.randint(0, t - 1)
        profile_matrix = profile([current_motifs[j]
                                 for j in range(t) if j != i])
        new_motifs = find_motifs(profile_matrix, dna, i)

        if score(new_motifs) < score(best_motifs):
            best_motifs = new_motifs.copy()

    return best_motifs


# Example usage
Dna = ["AAGCC",
       "TTACG",
       "GGGCG",
       "CACAG"]
k = 3
t = len(Dna)
N = 100

best_motifs = gibbs_sampler(Dna, k, t, N)
print("Best Motifs:", best_motifs)
