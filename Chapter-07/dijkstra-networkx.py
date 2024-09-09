import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges along with their weights
G.add_edge('start', 'a', weight=6)
G.add_edge('start', 'b', weight=2)
G.add_edge('a', 'fin', weight=1)
G.add_edge('b', 'a', weight=3)
G.add_edge('b', 'fin', weight=5)

# Compute the shortest path from 'start' to 'fin' using Dijkstra's algorithm
shortest_path = nx.dijkstra_path(G, source='start', target='fin')
shortest_path_length = nx.dijkstra_path_length(G, source='start', target='fin')

print("Shortest path:", shortest_path)
print("Shortest path length:", shortest_path_length)
