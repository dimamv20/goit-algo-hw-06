import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

Station = ['Jasper Avenue', 'Bebina2', 'Cinemiki3', 'Domeniko4']

G.add_edges_from([('Jasper Avenue', 'Bebina2'), ('Jasper Avenue', 'Cinemiki3'), ('Bebina2', 'Cinemiki3'), ('Bebina2', 'Domeniko4'), ('Cinemiki3', 'Domeniko4')])

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', linewidths=2, font_size=12, font_weight='bold')
plt.title('Граф міста')
plt.show()

print("Кількість Станцій:", len(Station))
print("Кількість ребер (доріг):", G.number_of_edges())
