from queue import PriorityQueue

def uniform_cost_search(graph, start_node, goal_node):
    visited = set()  # Set to keep track of visited nodes
    frontier = PriorityQueue()  # Priority queue to store nodes with their path cost
    frontier.put((0, start_node))  # Start node with path cost 0
    path = {start_node: None}  # Dictionary to store the paths, initialize start node with None

    while not frontier.empty():
        cost, current_node = frontier.get()

        if current_node == goal_node:
            # Goal node reached, construct the path
            return construct_path(path, start_node, goal_node)

        visited.add(current_node)

        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                new_cost = cost + neighbor_cost
                if neighbor not in path or new_cost < path[neighbor]:
                    path[neighbor] = current_node  # Store the parent node
                    frontier.put((new_cost, neighbor))

    # No path found
    return None


def construct_path(path, start_node, goal_node):
    current_node = goal_node
    path_list = [current_node]

    while current_node != start_node:
        current_node = path[current_node]
        path_list.append(current_node)

    path_list.reverse()
    return path_list


# Example graph represented as an adjacency list
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

start_node = 'A'
goal_node = 'G'

path = uniform_cost_search(graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found.")