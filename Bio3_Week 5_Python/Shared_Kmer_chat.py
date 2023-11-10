
'''
Shared k-mers Problem: Given two strings, find all their shared k-mers.
     Input: An integer k and two strings.
     Output: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions
     of these k-mers in the respective strings.

Sample Input:
3
AAACTCATC
TTTCAAATC
Sample Output:
(0, 4)
(0, 0)
(4, 2)
(6, 6)
'''


def shared_kmers(dna1, dna2, k):
    '''Returns a list of positions for shared kmers (up to reverse complement) in dna1 and dna2.'''

    def ReverseComplement(dna):
        '''Returns the reverse complement of a given DNA strand.'''
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement[base] for base in reversed(dna))

    # Initialize the dictionary to store kmers.
    dna_dict = {}

    # Store the starting index of all kmers contained in dna1 in a list keyed to the kmer.
    for i in range(len(dna1) - k + 1):
        # Add the ith kmer.
        if dna1[i:i+k] in dna_dict:
            dna_dict[dna1[i:i+k]].append(i)
        else:
            dna_dict[dna1[i:i+k]] = [i]

    # Add the reverse complement of the ith kmer.
        if ReverseComplement(dna1[i:i+k]) in dna_dict:
            dna_dict[ReverseComplement(dna1[i:i+k])].append(i)
        else:
            dna_dict[ReverseComplement(dna1[i:i+k])] = [i]

    # Use a set to remove possible duplicate entries.
    common_kmers = set()

# Check kmers in dna2 against those in dna1, adding matching indices to common_kmers.
    for j in range(len(dna2) - k + 1):
        # Check the jth kmer.
        if dna2[j:j+k] in dna_dict:
            for x in dna_dict[dna2[j:j+k]]:
                common_kmers.add((x, j))

        # Check the reverse complement of the jth kmer.
        if ReverseComplement(dna2[j:j+k]) in dna_dict:
            for x in dna_dict[ReverseComplement(dna2[j:j+k])]:
                common_kmers.add((x, j))
    return common_kmers


if __name__ == '__main__':

    # Read the input data.
    with open('Test2_Kmer.txt') as input_data:
        k = int(input_data.readline().strip())
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    # Get the shared kmers.  Sorting doesn't add significant time and makes the result more readable.
    common = map(str, sorted(shared_kmers(dna1, dna2, k)))

    # Print and save the answer.
    print('\n'.join(common))
    with open('result.txt', 'w') as output_data:
        output_data.write('\n'.join(common))
