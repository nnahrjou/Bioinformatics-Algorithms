from itertools import product

def is_compatible(column1, column2):
    for i in range(len(column1)):
        if column1[i] == 1 and column2[i] == 0:
            return False
    return True

def generate_compatible_columns(given_column):
    length = len(given_column)
    compatible_columns = []

    for combo in product([0, 1], repeat=length):
        if is_compatible(combo, given_column):
            compatible_columns.append(combo)

    return compatible_columns

# Given column
given_column = (1, 0, 1, 0, 1)

# Generate compatible columns
compatible_columns = generate_compatible_columns(given_column)

# Print the compatible columns
for column in compatible_columns:
    print(column)
