def generate_overlap_graph(patterns, k):
    overlap_graph = {}
    
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        
        if prefix not in overlap_graph:
            overlap_graph[prefix] = []
        
        overlap_graph[prefix].append(suffix)
    
    return overlap_graph

# Example usage
patterns = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]
k = len(patterns[0])
overlap_graph = generate_overlap_graph(patterns, k)

for node, neighbors in overlap_graph.items():
    print(f"{node} -> {', '.join(neighbors)}")
