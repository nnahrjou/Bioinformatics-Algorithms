# Something wrong in this code

def EulerianPath(adjacency_list):
    def find_start_end_nodes(graph):
        in_degree = {node: 0 for node in graph}
        out_degree = {node: 0 for node in graph}

        for node, neighbors in graph.items():
            out_degree[node] = len(neighbors)
            for neighbor in neighbors:
                in_degree[neighbor] += 1

        start_node = None
        end_node = None

        for node in graph:
            if in_degree[node] < out_degree[node]:
                start_node = node
            elif out_degree[node] < in_degree[node]:
                end_node = node

        if start_node is None and end_node is None:
            start_node = next(iter(graph))

        return start_node, end_node

    def eulerian_path_recursive(node, graph, path):
        while graph[node]:
            next_node = graph[node].pop(0)
            eulerian_path_recursive(next_node, graph, path)
        path.append(node)

    # Create a copy of the adjacency list to avoid modifying the input
    graph = {node: list(neighbors) for node, neighbors in adjacency_list.items()}
    start_node, end_node = find_start_end_nodes(graph)
    eulerian_path = []
    eulerian_path_recursive(start_node, graph, eulerian_path)
    eulerian_path.reverse()
    return eulerian_path

# Example input graph represented as an adjacency list
input_graph = {
    0: [2],
    1: [3],
    2: [1],
    3: [0, 4],
    6: [3, 7],
    7: [8],
    8: [9],
    9: [6]
}

# Solve the Eulerian Path Problem
eulerian_path = EulerianPath(input_graph)

# Print the Eulerian path
print("Eulerian Path:", " ".join(map(str, eulerian_path)))
