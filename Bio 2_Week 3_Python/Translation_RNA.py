def translate_rna_to_protein(rna, genetic_code):
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == "*":
                break  # Stop translation at stop codon
            protein += amino_acid
    return protein

def read_genetic_code(file_path):
    genetic_code = {}
    with open(file_path, 'r') as file:
        for line in file:
            codon, amino_acid = line.strip().split()
            genetic_code[codon] = amino_acid
    return genetic_code

# Specify the genetic code file path
genetic_code_path = "genetic_code.txt"

# Read the genetic code from the file
genetic_code = read_genetic_code(genetic_code_path)

# Example input
rna = "CCACGUACUGAAAUUAAC"

# Translate RNA to protein using the genetic code
translated_protein = translate_rna_to_protein(rna, genetic_code)
print("Translated Protein:", translated_protein)
