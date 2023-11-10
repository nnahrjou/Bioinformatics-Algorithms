def longest_path(graph, node, memo):
    if node not in memo:
        if node not in graph:
            memo[node] = ([node], 0)
        else:
            max_distance = 0
            max_path = []
            for neighbor, weight in graph[node].items():
                path, distance = longest_path(graph, neighbor, memo)
                if distance + weight > max_distance:
                    max_distance = distance + weight
                    max_path = path
            memo[node] = (max_path + [node], max_distance)
    return memo[node]


# Example graph with weights
graph = {
    'a': {'b': 3, 'c': 6, 'd': 5},
    'b': {'c': 2, 'f': 4},
    'c': {'e': 4, 'f': 3, 'g': 7},
    'd': {'e': 4, 'f': 5},
    'e': {'g': 2},
    'f': {'g': 1}
}

# Find the longest path for each node
memo = {}
longest_paths = {}
for node in graph.keys():
    longest_path_info = longest_path(graph, node, memo)
    longest_paths[node] = longest_path_info[0]

# Find the overall longest path
max_length = 0
max_path = []
for node, path in longest_paths.items():
    if len(path) > max_length:
        max_length = len(path)
        max_path = path

print("Longest path in order of the graph:", " -> ".join(max_path))
