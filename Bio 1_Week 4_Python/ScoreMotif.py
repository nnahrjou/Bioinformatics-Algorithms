def score_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)
    consensus_score = 0

    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        max_count = max(count.values())
        consensus_score += t - max_count

    return consensus_score


# Example usage
motifs = ["AAGCC",
          "TTACG",
          "GGGCG",
          "CACAG"]
score = score_motifs(motifs)
print("Consensus Score:", score)
