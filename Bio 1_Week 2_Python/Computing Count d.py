def HammingDistance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have equal length")

    distance = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1

    return distance


def ApproximatePatternCount(Text, Pattern, d):
    count = 0

    for i in range(len(Text) - len(Pattern) + 1):
        Pattern_prime = Text[i:i + len(Pattern)]

        if HammingDistance(Pattern, Pattern_prime) <= d:
            count += 1

    return count


# Example usage:
Text = "TTGTCTTCTGACCTCACCTGACAGCGCCCCCGAGGTTCTCGTGCGTCGGTATTTAATAAGAGCTGATTGTGGTAGTGCATGCGAGACAACCTTGCCCGTCACACGATCTCGGGACATCTAGCCCCCATGAAGCGCTGAATACTGCGCCCCAGAATCTGAACAGAGCTCCTCCTAAAGACGAGGAGCGAGAAGCGGATTTGTCCTCTCAATTCGTCAGATTAGACGTCAGGGATCCCAATTAGAGCCCATAGTGAAAACCTCAATACGGGGACTATGAGGACATCGATATGTCACGATGGAGAGGAAGAATGGTGATGTAGTCTAAATGAAGAGATGTAATGAGTCGCCTGAC"
Pattern = "GTGATGT"
d = 2
result = ApproximatePatternCount(Text, Pattern, d)
print("Approximate count:", result)
