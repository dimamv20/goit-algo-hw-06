from collections import deque
import networkx as nx

G = nx.Graph()
Station = ['Jasper Avenue', 'Bebina2', 'Cinemiki3', 'Domeniko4']
G.add_edges_from([('Jasper Avenue', 'Bebina2'), ('Jasper Avenue', 'Cinemiki3'), ('Bebina2', 'Cinemiki3'), ('Bebina2', 'Domeniko4'), ('Cinemiki3', 'Domeniko4')])

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]  
    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)  



def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)




start = 'Jasper Avenue'
print("Шляхи за допомогою DFS:")
dfs_iterative(G, start)
print()
print('-'*50)

print("Шляхи за допомогою BFS:")
bfs_iterative(G, start)
