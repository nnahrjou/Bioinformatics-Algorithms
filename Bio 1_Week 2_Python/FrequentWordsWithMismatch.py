def HammingDistance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have equal length")

    distance = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1

    return distance


def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    Neighborhood = set()

    SuffixNeighbors = Neighbors(Pattern[1:], d)

    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for x in 'ACGT':
                Neighborhood.add(x + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)

    return Neighborhood


def FrequentWordsWithMismatches(Text, k, d):
    Patterns = []
    freqMap = {}
    n = len(Text)

    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        neighborhood = Neighbors(Pattern, d)

        for neighbor in neighborhood:
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1

    m = max(freqMap.values())

    for Pattern in freqMap:
        if freqMap[Pattern] == m:
            Patterns.append(Pattern)

    return Patterns


# Example usage:
Text = "TGGTTGGTTGGTAAATGCGTGCGTGCTAAATCTTAAATAAATGCGTGCTGCTCTTGCGTTGGTTGGTCTTCTTGCTGCGTGCGTAAATCTTGCGTCTTGCGTCTTGCGTGCGTTGGTGCTTGGTCTTAAATCTTTGGTGCTCTTGCTCTTGCGTGCGTGCGTGCTGCGTTGGTAAATAAATGCTGCGTTGGTCTTTGGTGCTAAATGCTAAATCTTGCGTGCTGCGTGCTGCTGCTAAATGCGTGCTTGGTGCGTGCGTGCGTCTTAAATGCTGCGTTGGTCTTGCTCTTGCTCTTGCTGCGTCTTTGGTGCTTGGTGCGTCTTGCGTGCGTCTTGCTAAATCTTAAAT"
k = 5
d = 2
result = FrequentWordsWithMismatches(Text, k, d)
print("Frequent words with mismatches:", result)
