import math

# Number of mismatches allowed
max_mismatches = 4

# Length of the strings
string_length = 152

# Initialize k
k = 1

while True:
    # Calculate the number of ways to choose 4 positions from the k-mer
    combinations = math.comb(k, max_mismatches)
    
    # Calculate the number of possible k-mers in each string
    possible_kmers = string_length - k + 1
    
    # Check if there's at least one k-mer that satisfies the condition
    if combinations * possible_kmers >= 1:
        k += 1
    else:
        break

# Subtract 1 to get the largest k that satisfies the condition
largest_k = k - 1

print("Largest k:", largest_k)
