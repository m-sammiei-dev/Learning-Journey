def shortest_path(graph, start, target=''):
    """
    Compute the shortest paths in a weighted graph using Dijkstra's algorithm.

    Parameters:
        graph: A weighted graph represented as an adjacency list.
        start: The starting node.
        target: The destination node. If not provided, the function prints
            the shortest paths from the start node to all reachable nodes.

    Returns:
        distances: A dictionary mapping each node to its shortest distance
            from the start node.
        paths: A dictionary mapping each node to the shortest path
            from the start node.
    """


    unvisited = list(graph)

    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    
    paths = {node: [] for node in graph}
    paths[start] = [start] 

    while unvisited:
        # Select the unvisited node with the smallest known distance
        current = min(unvisited, key=distances.get)

        if distances[current] == float('inf'):
            break

        if target and current == target:
            break

        for neighbor, weight in graph[current]:
            new_distance = distances[current] + weight

            # If a shorter path is found, update distance and reconstruct path
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                paths[neighbor] = paths[current] + [neighbor]

        unvisited.remove(current)

    # Determine which nodes to print results for
    targets_to_print = [target] if target else graph

    # Display distances and paths
    for node in targets_to_print:
        if node == start:
            continue

        # Handle unreachable nodes gracefully
        if distances[node] == float('inf'):
            print(f"\n{start}-{node}: unreachable")
        else:
            print(f"\n{start}-{node} distance: {distances[node]}")
            print(f"Path: {' -> '.join(paths[node])}")

    return distances, paths


my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


shortest_path(my_graph, 'A', 'F')