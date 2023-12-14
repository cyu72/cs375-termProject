import random
def dfs(graph, start):
    visited = set()  # To keep track of visited nodes
    visit_count = {node: 0 for node in graph}  # Initialize visit count for each node
    stack = [start]  # Stack for DFS, initialized with the start node

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            visit_count[current_node] += 1

            # Add all unvisited neighbors to the stack
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        # Break when the stack is empty (end of the current wave)
        if not stack:
            break

    return visit_count

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
total_visit_count = {node: 0 for node in graph}
for _ in range(10000):
    start_node = random.choice(list(graph.keys()))
    visit_count = dfs(graph, start_node)
    for node in visit_count:
        total_visit_count[node] += visit_count[node]

# Calculate the total number of visits across all nodes
total_visits = sum(total_visit_count.values())

# Calculate the percentage visit count for each node
percentage_visit_count = {node: (count / total_visits * 100) for node, count in total_visit_count.items()}

# Print the percentage visit count for each node
print("Percentage Visit Count:")
for node, percentage in percentage_visit_count.items():
    print(f"{node}: {percentage:.2f}%")
