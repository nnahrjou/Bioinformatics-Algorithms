def build_suffix_array(text):
    text += "$"  # Add a sentinel character to ensure uniqueness of all suffixes
    n = len(text)
    
    # Create a list of tuples (suffix, original_index) to store suffixes and their corresponding original indices
    suffixes = [(text[i:], i) for i in range(n)]
    
    # Sort the list of suffixes lexicographically
    suffixes.sort()
    
    # Extract the sorted indices to get the suffix array
    suffix_array = [suffix[1] for suffix in suffixes]
    
    return suffix_array

# Input
text = "papaya$"

# Compute the suffix array
suffix_array = build_suffix_array(text)

# Output as a space-separated string
output = " ".join(map(str, suffix_array))
print(output)
