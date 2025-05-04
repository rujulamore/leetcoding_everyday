def topological_sort(nodes, edges):
    """
    Perform topological sort on a directed graph using DFS approach.
    
    Args:
        nodes: List of nodes in the graph
        edges: List of tuples representing directed edges (from, to)
    
    Returns:
        List of nodes in topologically sorted order or None if cycle is detected
    """
    # Build adjacency list
    graph = {node: [] for node in nodes}
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
    
    L = []  # Will contain the sorted nodes
    permanent = set()
    temporary = set()
    cycle_detected = False
    
    def visit(n):
        nonlocal cycle_detected
        if n in permanent:
            return
        if n in temporary:
            cycle_detected = True
            return
        
        temporary.add(n)
        
        for m in graph.get(n, []):
            visit(m)
            if cycle_detected:
                return
        
        temporary.remove(n)
        permanent.add(n)
        L.insert(0, n)  # Add to head of list
    
    while len(permanent) < len(nodes) and not cycle_detected:
        for node in nodes:
            if node not in permanent and node not in temporary:
                visit(node)
                if cycle_detected:
                    break
    
    return L if not cycle_detected else None

# Example usage
if __name__ == "__main__":
    # Example 1: Acyclic graph
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'D'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('D', 'E'), ('E', 'F')]
    
    print("Example 1 (Acyclic graph):")
    sorted_order = topological_sort(nodes, edges)
    print("Topological order:", sorted_order)
    
    # Example 2: Cyclic graph
    nodes_cyclic = ['A', 'B', 'C']
    edges_cyclic = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    
    print("\nExample 2 (Cyclic graph):")
    sorted_order_cyclic = topological_sort(nodes_cyclic, edges_cyclic)
    print("Result:", sorted_order_cyclic)