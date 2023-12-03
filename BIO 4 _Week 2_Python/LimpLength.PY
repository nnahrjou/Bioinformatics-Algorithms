def limb_length(n, j, distance_matrix):
    limb_lengths = []

    for i in range(n):
        for k in range(n):
            if i != j and k != j:
                limb = (distance_matrix[i][j] + distance_matrix[j][k] - distance_matrix[i][k]) / 2
                limb_lengths.append(limb)

    return min(limb_lengths)

# Read input from a file
with open('TEST1.txt', 'r') as f:
    n = int(f.readline())
    j = int(f.readline())
    distance_matrix = []
    for _ in range(n):
        row = list(map(int, f.readline().split()))
        distance_matrix.append(row)

# Calculate the limb length
result = limb_length(n, j, distance_matrix)

# Print the result
print(result)
