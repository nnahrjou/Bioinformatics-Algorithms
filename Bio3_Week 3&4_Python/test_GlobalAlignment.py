def global_alignment_affine_gap_penalty(v, w, score_matrix, gap_opening_penalty, gap_extension_penalty):
    n = len(v)
    m = len(w)

    # Initialize the DP tables
    M = [[0] * (m + 1) for _ in range(n + 1)]  # Match/Mismatch table
    X = [[0] * (m + 1) for _ in range(n + 1)]  # Gap in v table
    Y = [[0] * (m + 1) for _ in range(n + 1)]  # Gap in w table

    # Initialize the traceback tables
    backtrack_m = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack_x = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack_y = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill in the DP tables
    for i in range(1, n + 1):
        M[i][0] = -gap_opening_penalty - (i - 1) * gap_extension_penalty
        X[i][0] = -gap_opening_penalty - (i - 1) * gap_extension_penalty
        Y[i][0] = -float('inf')

    for j in range(1, m + 1):
        M[0][j] = -gap_opening_penalty - (j - 1) * gap_extension_penalty
        X[0][j] = -float('inf')
        Y[0][j] = -gap_opening_penalty - (j - 1) * gap_extension_penalty

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = M[i - 1][j - 1] + score_matrix[v[i - 1]][w[j - 1]]
            x_gap = max(M[i - 1][j] - gap_opening_penalty - gap_extension_penalty,
                        X[i - 1][j] - gap_extension_penalty)
            y_gap = max(M[i][j - 1] - gap_opening_penalty - gap_extension_penalty,
                        Y[i][j - 1] - gap_extension_penalty)

            M[i][j] = max(match, x_gap, y_gap)
            X[i][j] = max(M[i - 1][j] - gap_opening_penalty -
                          gap_extension_penalty, X[i - 1][j] - gap_extension_penalty)
            Y[i][j] = max(M[i][j - 1] - gap_opening_penalty -
                          gap_extension_penalty, Y[i][j - 1] - gap_extension_penalty)

            if M[i][j] == match:
                backtrack_m[i][j] = "M"
            if M[i][j] == x_gap:
                backtrack_m[i][j] = "X"
            if M[i][j] == y_gap:
                backtrack_m[i][j] = "Y"

            if X[i][j] == M[i - 1][j] - gap_opening_penalty - gap_extension_penalty:
                backtrack_x[i][j] = "M"
            if X[i][j] == X[i - 1][j] - gap_extension_penalty:
                backtrack_x[i][j] = "X"

            if Y[i][j] == M[i][j - 1] - gap_opening_penalty - gap_extension_penalty:
                backtrack_y[i][j] = "M"
            if Y[i][j] == Y[i][j - 1] - gap_extension_penalty:
                backtrack_y[i][j] = "Y"

    # Find the maximum alignment score
    max_alignment_score = M[n][m]

    # Traceback to construct the alignment
    i, j = n, m
    aligned_v = []
    aligned_w = []
    current_backtrack = "M"
    while i > 0 or j > 0:
        if current_backtrack == "M":
            if backtrack_m[i][j] == "M":
                aligned_v.append(v[i - 1])
                aligned_w.append(w[j - 1])
                i -= 1
                j -= 1
            elif backtrack_m[i][j] == "X":
                current_backtrack = "X"
            elif backtrack_m[i][j] == "Y":
                current_backtrack = "Y"
        elif current_backtrack == "X":
            if backtrack_x[i][j] == "M":
                aligned_v.append(v[i - 1])
                aligned_w.append('-')
                i -= 1
            elif backtrack_x[i][j] == "X":
                i -= 1
        elif current_backtrack == "Y":
            if backtrack_y[i][j] == "M":
                aligned_v.append('-')
                aligned_w.append(w[j - 1])
                j -= 1
            elif backtrack_y[i][j] == "Y":
                j -= 1

    aligned_v.reverse()
    aligned_w.reverse()

    aligned_v_str = ''.join(aligned_v)
    aligned_w_str = ''.join(aligned_w)

    return max_alignment_score, aligned_v_str, aligned_w_str


# Example usage
score_matrix = {
    'A': {'A': 1, 'C': -1, 'G': -1, 'T': -1},
    'C': {'A': -1, 'C': 1, 'G': -1, 'T': -1},
    'G': {'A': -1, 'C': -1, 'G': 1, 'T': -1},
    'T': {'A': -1, 'C': -1, 'G': -1, 'T': 1}
}

gap_opening_penalty = 2
gap_extension_penalty = 1

v = "GA"
w = "GTTA"

alignment_score, aligned_v, aligned_w = global_alignment_affine_gap_penalty(
    v, w, score_matrix, gap_opening_penalty, gap_extension_penalty)

print("Alignment score:", alignment_score)
print("Aligned v:", aligned_v)
print("Aligned w:", aligned_w)
