def reconstruct_string_from_genome_path(patterns):
    text = patterns[0]  # Initialize the reconstructed string with the first k-mer

    # Iterate through the remaining k-mers in the genome path
    for pattern in patterns[1:]:
        # Add the last character of the current k-mer to the reconstructed string
        text += pattern[-1]

    return text

# Example usage
patterns = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
reconstructed_text = reconstruct_string_from_genome_path(patterns)
print(reconstructed_text)
