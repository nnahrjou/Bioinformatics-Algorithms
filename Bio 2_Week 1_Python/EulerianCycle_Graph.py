import random

def EulerianCycle(Graph):
    def random_walk(node, unexplored_edges):
        cycle = [node]
        while unexplored_edges[node]:
            next_node = unexplored_edges[node].pop()
            cycle.append(next_node)
            node = next_node
        return cycle
    
    unexplored_edges = {node: list(neighbors) for node, neighbors in Graph.items()}
    start_node = random.choice(list(Graph.keys()))
    cycle = random_walk(start_node, unexplored_edges)
    
    while any(unexplored_edges.values()):
        for node in cycle:
            if unexplored_edges[node]:
                start_node = node
                break
        new_cycle = random_walk(start_node, unexplored_edges)
        index = cycle.index(start_node)
        cycle = cycle[:index] + new_cycle + cycle[index+1:]
    
    return cycle

# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
}

eulerian_cycle = EulerianCycle(graph)
print("Eulerian Cycle:", eulerian_cycle)
