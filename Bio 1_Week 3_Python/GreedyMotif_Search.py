def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def profile_most_probable_kmer(text, k, profile):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    max_prob = -1
    most_probable = ""

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1.0

        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotides[nucleotide]][j]

        if prob > max_prob:
            max_prob = prob
            most_probable = kmer

    return most_probable


def form_profile(motifs):
    profile = []
    k = len(motifs[0])

    for j in range(k):
        col = [motif[j] for motif in motifs]
        counts = {'A': 1, 'C': 1, 'G': 1, 'T': 1}

        for nucleotide in col:
            counts[nucleotide] += 1

        profile_col = [counts['A'] / (len(motifs) + 4), counts['C'] / (len(motifs) + 4),
                       counts['G'] / (len(motifs) + 4), counts['T'] / (len(motifs) + 4)]
        profile.append(profile_col)

    return profile


def score_motifs(motifs):
    consensus = ""

    for j in range(len(motifs[0])):
        col = [motif[j] for motif in motifs]
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for nucleotide in col:
            counts[nucleotide] += 1

        consensus += max(counts, key=counts.get)

    score = sum(hamming_distance(motif, consensus) for motif in motifs)
    return score


def greedy_motif_search(Dna, k, t):
    best_motifs = [seq[:k] for seq in Dna]

    for i in range(len(Dna[0]) - k + 1):
        motifs = [Dna[j][i:i + k] for j in range(t)]

        for j in range(1, t):
            profile = form_profile(motifs[:j])
            most_probable_kmer = profile_most_probable_kmer(Dna[j], k, profile)
            motifs[j] = most_probable_kmer

        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs

    return best_motifs


# New example usage
k = 4
t = 4
Dna = ["ACTGAGG", "GGTAGGG", "ATCGAGG", "AAGGAGG"]

result = greedy_motif_search(Dna, k, t)
for motif in result:
    print(motif)
