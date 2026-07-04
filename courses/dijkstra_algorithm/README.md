# Dijkstra's Shortest Path Algorithm

A simple, readable implementation of **Dijkstra's algorithm** in pure Python (no external libraries) for finding the shortest path between nodes in a weighted graph.

## 📊 Example Graph

<div align="center">
<table>
<tr>
<td align="center">
<img src="graph_example.svg" alt="Weighted graph with shortest path A to F highlighted" width="500"/>
<br/>
<sub><b>Figure 1.</b> The weighted graph defined in <code>my_graph</code>. The red path shows the shortest route from <code>A</code> to <code>F</code> (distance = 6), computed by the algorithm below.</sub>
</td>
</tr>
</table>
</div>

## ✨ Features

- Computes the shortest distance from a start node to every other node
- Reconstructs and displays the **actual path taken**, not just the final distance
- Supports limiting the output to a single target node
- Stops early once the target is reached, or once remaining nodes are unreachable
- Handles unreachable nodes gracefully instead of crashing
- Documented with a clear docstring
- No external dependencies — pure Python only

## 🧠 How the Algorithm Works

1. The graph is defined as a dictionary mapping each node to a list of `(neighbor, edge_weight)` pairs.
2. The start node's distance is set to zero, and all other nodes are initialized to infinity.
3. At each step, the closest unvisited node is selected.
4. **Early exit #1:** if that node's distance is still infinity, every remaining node is unreachable — the loop stops.
5. **Early exit #2:** if a specific `target` was requested and it has just been reached, the loop stops — no need to keep exploring the rest of the graph.
6. Otherwise, the node's neighbors are relaxed: if a shorter path to a neighbor is found, its distance and path are updated.
7. The processed node is removed from the unvisited list, and the loop repeats until it's empty (or an early exit triggers).

## ⏱️ Time Complexity

This implementation selects the next node with `min(unvisited, key=distances.get)`, which is a **linear scan** over the unvisited list rather than a priority queue. That gives:

- **Current implementation:** `O(V² + E)` — where `V` is the number of vertices and `E` is the number of edges.
- **Optimized version (with a binary heap / `heapq`):** `O((V + E) log V)`

In practice, the two early-exit checks (unreachable nodes, and reaching a specific `target`) often mean the loop finishes well before visiting every node, even without a heap.

## 🚀 Usage

```python
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

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Compute the shortest path from A to F only (stops as soon as F is reached)
shortest_path(my_graph, 'A', 'F')

# Compute the shortest path from A to all nodes
shortest_path(my_graph, 'A')
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `graph` | `dict` | required | Graph in the form `{node: [(neighbor, weight), ...]}`. Directed by default — add edges in both directions for an undirected graph. |
| `start` | `str` | required | The starting node. |
| `target` | `str` | `''` | The target node. If empty, distances and paths to **all** nodes are printed. |

### Return Value

The function returns a tuple `(distances, paths)`:

- `distances` (`dict`): the shortest distance from `start` to each node (`float('inf')` if unreachable)
- `paths` (`dict`): the list of nodes forming the shortest path from `start` to each node (`[]` if unreachable)

## 🚧 Unreachable Nodes

If a node can't be reached from `start`, it isn't treated as an error — it's reported directly in the printed output:

```
A-X: unreachable
```

## 📄 Sample Output

Running `shortest_path(my_graph, 'A', 'F')` on the example graph above prints:

```
A-F distance: 6
Path: A -> C -> B -> F
```

This matches the highlighted path in Figure 1: **A → C → B → F**.

## 📦 Running the Project

No packages need to be installed — just make sure Python 3 is available:

```bash
python shortest_path.py
```

## 📄 License

This project is released under the MIT License. Feel free to use, modify, and distribute it.

---
**Developed by Mohammad Sammiei**  
*Junior Developer & AI Student*
