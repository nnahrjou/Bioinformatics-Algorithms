def generate_de_bruijn_graph(patterns):
    de_bruijn_graph = {}
    
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        
        if prefix not in de_bruijn_graph:
            de_bruijn_graph[prefix] = []
        
        de_bruijn_graph[prefix].append(suffix)
    
    return de_bruijn_graph

# Example usage
# Read DNA sequences from a text file
with open("dataset_3.txt", "r") as file:
    patterns = [line.strip() for line in file]
# patterns = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]

de_bruijn_graph = generate_de_bruijn_graph(patterns)

for node, neighbors in de_bruijn_graph.items():
    print(f"{node} -> {', '.join(neighbors)}")


