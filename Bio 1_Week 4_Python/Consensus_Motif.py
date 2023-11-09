def find_consensus_motif(motifs):
    k = len(motifs[0])
    consensus_motif = ""

    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        consensus_nucleotide = max(count, key=count.get)
        consensus_motif += consensus_nucleotide

    return consensus_motif


# Example usage
motifs = ["AAGCC",
          "TTACG",
          "GGGCG",
          "CACAG"]
consensus = find_consensus_motif(motifs)
print("Consensus Motif:", consensus)
