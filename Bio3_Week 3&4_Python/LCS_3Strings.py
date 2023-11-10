def sequence_alignment(str1, str2, str3, match_score, mismatch_penalty, gap_penalty):
    m, n, o = len(str1), len(str2), len(str3)
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + match_score
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1]
                    )

    alignment_score = dp[m][n][o]
    aligned_sequences = []

    i, j, k = m, n, o
    while i > 0 and j > 0 and k > 0:
        if str1[i - 1] == str2[j - 1] == str3[k - 1]:
            aligned_sequences.append(str1[i - 1])
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j][k] >= dp[i][j - 1][k] and dp[i - 1][j][k] >= dp[i][j][k - 1]:
            i -= 1
        elif dp[i][j - 1][k] >= dp[i - 1][j][k] and dp[i][j - 1][k] >= dp[i][j][k - 1]:
            j -= 1
        else:
            k -= 1

    aligned_sequences.reverse()
    aligned_string = ''.join(aligned_sequences)

    return aligned_string, alignment_score


# Input strings
string1 = "CCAATACGAC"
string2 = "GCCTTACGCT"
string3 = "CCCTAGCGGC"

# Penalty values
match_score = 1
mismatch_penalty = -1
gap_penalty = -2

# Find and print the aligned sequence and alignment score
aligned_sequence, alignment_score = sequence_alignment(
    string1, string2, string3, match_score, mismatch_penalty, gap_penalty)
print("Aligned Sequence:", aligned_sequence)
print("Alignment Score:", alignment_score)
