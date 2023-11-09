def generate_de_bruijn_graph(k, text):
    de_bruijn_graph = {}
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prefix = kmer[:-1]
        suffix = kmer[1:]
        
        if prefix not in de_bruijn_graph:
            de_bruijn_graph[prefix] = []
        
        de_bruijn_graph[prefix].append(suffix)
    
    return de_bruijn_graph

# Example usage
k = 4
text = "AAGATTCTCTAC"
de_bruijn_graph = generate_de_bruijn_graph(k, text)

for node, neighbors in de_bruijn_graph.items():
    print(f"{node} -> {', '.join(neighbors)}")
