import networkx as nx

G = nx.Graph()
Station = ['Jasper Avenue', 'Bebina2', 'Cinemiki3', 'Domeniko4']
G.add_edges_from([
    ('Jasper Avenue', 'Bebina2', {'weight': 3}),
    ('Jasper Avenue', 'Cinemiki3', {'weight': 1}),
    ('Bebina2', 'Cinemiki3', {'weight': 4}), 
    ('Bebina2', 'Domeniko4', {'weight': 3}),
    ('Cinemiki3', 'Domeniko4', {'weight': 2})
])


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = set(graph.nodes())
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_vertex)
        
        for neighbor in graph.neighbors(current_vertex):
            distance = distances[current_vertex] + graph[current_vertex][neighbor]['weight']
           
            if distance < distances[neighbor]:
                distances[neighbor] = distance



    return distances





# the most shortest distance for any station 
for node in G.nodes():
    shortest_distances = dijkstra(G, node)
    print(f"The most shortest distances from {node}: {shortest_distances}")
