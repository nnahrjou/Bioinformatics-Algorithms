def MaximalNonBranchingPaths(graph):
    def out_degree(node):
        return len(graph[node])

    def in_degree(node):
        count = 0
        for _, neighbors in graph.items():
            if node in neighbors:
                count += 1
        return count

    def is_one_in_one_out(node):
        return in_degree(node) == 1 and out_degree(node) == 1

    def get_one_in_one_out_node():
        for node in graph:
            if is_one_in_one_out(node):
                return node
        return None

    def extend_path(path, start):
        non_branching_path = [start]
        next_node = graph[start][0]
        while is_one_in_one_out(next_node):
            non_branching_path.append(next_node)
            next_node = graph[next_node][0]
        non_branching_path.append(next_node)
        return non_branching_path

    def remove_path(path):
        for node in path:
            if node in graph:
                del graph[node]

    paths = []

    while len(graph) > 0:
        one_in_one_out_node = get_one_in_one_out_node()

        if one_in_one_out_node:
            path = extend_path([], one_in_one_out_node)
            paths.append(path)
            remove_path(path)
        else:
            start_node = next(iter(graph))
            while out_degree(start_node) > 0:
                path = extend_path([], start_node)
                paths.append(path)
                remove_path(path)

    return paths


# Example usage
graph = {
    1: [2],
    2: [3],
    3: [4, 5],
    6: [7],
    7: [6]
}
result = MaximalNonBranchingPaths(graph)
for path in result:
    print(" -> ".join(map(str, path)))
