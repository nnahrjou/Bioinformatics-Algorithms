def inverse_burrows_wheeler_transform(bwt):
    n = len(bwt)
    
    # Create a list of pairs (character, index)
    pairs = [(bwt[i], i) for i in range(n)]
    
    # Sort the list lexicographically
    pairs.sort()
    
    # Find the row where the sentinel character ('$') is located
    for i, pair in enumerate(pairs):
        if pair[0] == "$":
            sentinel_row = i
            break
    
    # Reconstruct the original string starting from the character before '$'
    original_string = []
    current_row = sentinel_row
    
    while len(original_string) < n:
        original_string.append(pairs[current_row][0])
        current_row = pairs[current_row][1]
    
    # Convert the list to a string
    original_string = "".join(original_string)
    
    return original_string

# Input (BWT of the original string)
bwt = "TTCCATTGGA$"

# Compute the inverted BWT to recover the original string
original_text = inverse_burrows_wheeler_transform(bwt)

# Output
print(original_text)
