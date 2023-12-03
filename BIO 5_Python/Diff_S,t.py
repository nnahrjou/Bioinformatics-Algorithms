# Given SNP vectors
s = [0, 0, 1, 1, 0, 0, 1, 0]
t = [1, 1, 0, 0, 1, 1, 1, 1]

# Initialize variables
count_si_neq_sj = 0
count_ti_neq_tj = 0

# Iterate through all pairs of individuals (i, j)
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] != s[j] and t[i] != t[j]:
            count_si_neq_sj += 1
        if t[i] != t[j]:
            count_ti_neq_tj += 1

# Calculate Diff(s, t) for si ≠ sj and ti ≠ tj
Diff_si_neq_sj_ti_neq_tj = count_si_neq_sj / count_ti_neq_tj

print("Diff(s, t) for si ≠ sj and ti ≠ tj =", Diff_si_neq_sj_ti_neq_tj)
