import numpy as np
import time as time

def pagerank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    """
    Calculate PageRank for a given graph.

    Parameters:
    - graph: Dictionary representing the graph, where keys are nodes and values are lists of nodes
      representing outgoing edges.
    - damping_factor: Damping factor (usually set to 0.85).
    - max_iterations: Maximum number of iterations for the power iteration method.
    - tolerance: Convergence tolerance.

    Returns:
    - Dictionary where keys are nodes and values are their corresponding PageRank scores.
    """

    num_nodes = len(graph)
    initial_pagerank = 1.0 / num_nodes
    pagerank_vector = np.full(num_nodes, initial_pagerank)
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    # Build the adjacency matrix
    for i, node in enumerate(graph):
        for neighbor in graph[node]:
            adjacency_matrix[i, list(graph.keys()).index(neighbor)] = 1

    # Normalize the adjacency matrix
    row_sums = adjacency_matrix.sum(axis=1, keepdims=True)
    transition_matrix = adjacency_matrix / row_sums

    # Iterates through number of iterations, checking for convergence
    for _ in range(max_iterations):
        new_pagerank_vector = ((1 - damping_factor) / num_nodes) + damping_factor * np.dot(transition_matrix.T, pagerank_vector)

        # Check for convergence
        if np.linalg.norm(new_pagerank_vector - pagerank_vector, 2) < tolerance:
            break

        pagerank_vector = new_pagerank_vector

    # Maps pageRank scores to nodes in dictionary
    pagerank_scores = {node: score for node, score in zip(graph.keys(), pagerank_vector)}
    pagerank_sorted = dict(sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True))

    return pagerank_sorted

def construct_adjacency_matrix(file_path):
    adjacency_matrix = {}
    with open(file_path, 'r') as file:
        for line in file:
            x, y = line.split()
            if x not in adjacency_matrix:
                adjacency_matrix[x] = []
            adjacency_matrix[x].append(y)
            if y not in adjacency_matrix:
                adjacency_matrix[y] = []
            adjacency_matrix[y].append(x)
    return adjacency_matrix

file_path = "random_pairs.txt"
graph = construct_adjacency_matrix(file_path)
pagerank_scores = pagerank(graph)
print("PageRank scores:", pagerank_scores)
