import itertools

def is_compatible(column):
    for i in range(len(column)):
        for j in range(i+1, len(column)):
            if (column[i] == 1 and column[j] == 0) or (column[i] == 0 and column[j] == 1) or (column[i] == 1 and column[j] == 1):
                return False  # Incompatible if (1,0), (0,1), or (1,1) combinations found
    return True

# Given column
given_column = [1, 1, 1, 0, 1]

# Generate all possible columns of length 5
possible_columns = list(itertools.product([0, 1], repeat=5))

# Filter compatible columns
compatible_columns = [column for column in possible_columns if is_compatible(column)]

# Count the number of compatible columns
num_compatible_columns = len(compatible_columns)

print(f"Number of compatible columns: {num_compatible_columns}")
