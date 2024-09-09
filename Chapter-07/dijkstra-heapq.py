import heapq

def dijkstra(graph, start):
    # Initialize the priority queue
    priority_queue = [(0, start)]
    # Initialize the distances dictionary with infinite distance
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    # Initialize the parents dictionary to reconstruct the path
    parents = {vertex: None for vertex in graph}
    # Set to keep track of visited nodes
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current vertex has been visited, skip it
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parents

def get_path(parents, goal):
    path = []
    while goal:
        path.append(goal)
        goal = parents[goal]
    path.reverse()
    return path

# Example usage
graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {}
}

distances, parents = dijkstra(graph, 'start')
goal = 'fin'
path = get_path(parents, goal)

print("Distances:", distances)
print("Parents:", parents)
print("Path to goal:", path)
