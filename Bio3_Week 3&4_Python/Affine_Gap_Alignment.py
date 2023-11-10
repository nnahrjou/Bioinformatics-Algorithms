def affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w):
    n = len(v)
    m = len(w)

    # Initialize the matrices for the three DP tables
    M = [[0] * (m + 1) for _ in range(n + 1)]  # Match/Mismatch table
    X = [[0] * (m + 1) for _ in range(n + 1)]  # Gap in v table
    Y = [[0] * (m + 1) for _ in range(n + 1)]  # Gap in w table

    # Fill in the DP tables
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = M[i - 1][j - 1] + \
                (match_reward if v[i - 1] == w[j - 1] else -mismatch_penalty)
            x_gap = max(M[i - 1][j] - gap_opening_penalty - (i - 1) * gap_extension_penalty,
                        X[i - 1][j] - gap_extension_penalty)
            y_gap = max(M[i][j - 1] - gap_opening_penalty - (j - 1) * gap_extension_penalty,
                        Y[i][j - 1] - gap_extension_penalty)

            M[i][j] = max(match, x_gap, y_gap)
            X[i][j] = max(M[i - 1][j] - gap_opening_penalty -
                          gap_extension_penalty, X[i - 1][j] - gap_extension_penalty)
            Y[i][j] = max(M[i][j - 1] - gap_opening_penalty -
                          gap_extension_penalty, Y[i][j - 1] - gap_extension_penalty)

    # Find the maximum alignment score
    max_alignment_score = M[n][m]

    # Traceback to find the alignment
    i, j = n, m
    aligned_v = []
    aligned_w = []
    while i > 0 and j > 0:
        if i > 0 and j > 0 and M[i][j] == M[i - 1][j - 1] + (match_reward if v[i - 1] == w[j - 1] else -mismatch_penalty):
            aligned_v.append(v[i - 1])
            aligned_w.append(w[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and M[i][j] == X[i][j]:
            aligned_v.append(v[i - 1])
            aligned_w.append('-')
            i -= 1
        else:
            aligned_v.append('-')
            aligned_w.append(w[j - 1])
            j -= 1

    while i > 0:
        aligned_v.append(v[i - 1])
        aligned_w.append('-')
        i -= 1

    while j > 0:
        aligned_v.append('-')
        aligned_w.append(w[j - 1])
        j -= 1

    aligned_v.reverse()
    aligned_w.reverse()

    aligned_v_str = ''.join(aligned_v)
    aligned_w_str = ''.join(aligned_w)

    return max_alignment_score, aligned_v_str, aligned_w_str


# Read input from a text file
with open('Affine_Gap_Alignment.txt', 'r') as input_file:
    match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty = map(
        int, input_file.readline().split())
    v = input_file.readline().strip()
    w = input_file.readline().strip()

# Calculate the alignment
alignment_score, aligned_v, aligned_w = affine_gap_alignment(
    match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w)

# Write output to a text file
with open('output.txt', 'w') as output_file:
    output_file.write(str(alignment_score) + '\n')
    output_file.write(aligned_v + '\n')
    output_file.write(aligned_w + '\n')

print("Maximum alignment score and aligned sequences written to 'output.txt'.")
