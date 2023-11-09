def FrequencyTable(Text, k):
    freqMap = {}
    n = len(Text)

    for i in range(n - k + 1):
        Pattern = Text[i:i + k]

        if Pattern not in freqMap:
            freqMap[Pattern] = 1
        else:
            freqMap[Pattern] += 1

    return freqMap


def FindClumps(Text, k, L, t):
    Patterns = []  # An array to store the resulting patterns

    n = len(Text)
    # Loop through every window of length L in Text
    for i in range(n - L + 1):
        Window = Text[i:i + L]  # Extract the current window

        # Calculate the frequency of each k-mer within the current window
        freqMap = FrequencyTable(Window, k)

        # Check if the frequency of any k-mer is greater than or equal to t
        for s in freqMap:
            if freqMap[s] >= t:
                Patterns.append(s)

    # Remove duplicates from Patterns
    Patterns = list(set(Patterns))

    return Patterns


# Example usage:
Text = "AAACCCAAATTTGGG"
k = 3
L = 15
t = 3
result = FindClumps(Text, k, L, t)
print(result)
