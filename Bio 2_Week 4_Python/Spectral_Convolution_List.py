# Function to compute the convolution of a spectrum
def spectral_convolution(spectrum):
    convolution = {}
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            if i != j:
                diff = abs(spectrum[i] - spectrum[j])
                if diff != 0:  # Exclude zero differences
                    convolution[diff] = convolution.get(diff, 0) + 1
    convolution_list = [key for key, value in convolution.items() for _ in range(value)]
    return convolution_list

# Manual input for the sample case
spectrum_input = "0 137 186 323"
spectrum = list(map(int, spectrum_input.split()))

# Calculate and print the convolution
convolution = spectral_convolution(spectrum)
convolution.sort()  # Sort the convolution list
print(*convolution)  # Print the elements of the convolution separated by spaces
