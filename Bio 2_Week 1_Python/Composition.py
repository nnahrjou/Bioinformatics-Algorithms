def Composition3(dna_sequence, k):
    k_mers = [dna_sequence[i:i+k] for i in range(len(dna_sequence) - k + 1)]
    return k_mers

sequence = "TATGGGGTGC"
k = 3
result = Composition3(sequence, k)
print(result)
