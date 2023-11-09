from collections import Counter


# def FrequentWords(Text, k):
#     # Initialize an empty list to store the frequent k-mers
#     frequent_patterns = []

#     # Iterate through the text to find all k-mers of length k
#     for i in range(len(Text) - k + 1):
#         pattern = Text[i:i + k]
#         # Count the occurrences of the current k-mer
#         pattern_count = Counter(Text)[pattern]
#         # If it's the first occurrence, initialize the max_count variable
#         if i == 0:
#             max_count = pattern_count
#         # If the count of the current k-mer is greater than the max_count, update max_count
#         if pattern_count > max_count:
#             max_count = pattern_count

#     # Find all k-mers with count equal to max_count and add them to the frequent_patterns list
#     for i in range(len(Text) - k + 1):
#         pattern = Text[i:i + k]
#         pattern_count = Counter(Text)[pattern]
#         if pattern_count == max_count:
#             frequent_patterns.append(pattern)

#     # Remove duplicates and return the frequent k-mers
#     return list(set(frequent_patterns))


# Example usage:
# input_text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# k_value = 4

# result = FrequentWords(input_text, k_value)
# print("Frequent k-mers:", result)


def FrequencyTable(Text, k):
    freqMap = {}  # An empty dictionary to store the frequency map
    n = len(Text)

    for i in range(n - k + 1):
        Pattern = Text[i:i + k]  # Extract the k-mer from Text

        # If Pattern is not already in the freqMap, add it with a frequency of 1.
        # Otherwise, increment its frequency by 1.
        if Pattern not in freqMap:
            freqMap[Pattern] = 1
        else:
            freqMap[Pattern] += 1

    return freqMap


def MaxMap(freqMap):
    return max(freqMap.values())


def BetterFrequentWords(Text, k):
    frequentPatterns = []
    freqMap = FrequencyTable(Text, k)
    max_freq = MaxMap(freqMap)

    for pattern in freqMap:
        if freqMap[pattern] == max_freq:
            frequentPatterns.append(pattern)

    return frequentPatterns


# Example usage:
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
result = BetterFrequentWords(text, k)
print(result)
