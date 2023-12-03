def burrows_wheeler_transform(text):
    # Generate all cyclic permutations of the input string
    cyclic_permutations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort the cyclic permutations lexicographically
    cyclic_permutations.sort()
    
    # Extract the last character of each sorted cyclic permutation
    bwt = "".join(perm[-1] for perm in cyclic_permutations)
    
    return bwt

# Input
text = "CGTTTGCTAT$"

# Compute the Burrows-Wheeler Transform
bwt = burrows_wheeler_transform(text)

# Output
print(bwt)
