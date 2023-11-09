# Function to calculate the convolution of a spectrum
def spectral_convolution(spectrum):
    convolution = {}
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            if i != j:
                diff = abs(spectrum[i] - spectrum[j])
                if diff != 0:  # Exclude zero differences
                    convolution[diff] = convolution.get(diff, 0) + 1
    return convolution

# Example spectrum
spectrum = [0, 86, 160, 234, 308, 320, 382]

# Calculate the spectral convolution
convolution = spectral_convolution(spectrum)

# Print the differences and their multiplicities
for diff, multiplicity in convolution.items():
    print(f"Difference: {diff}, Multiplicity: {multiplicity}")
