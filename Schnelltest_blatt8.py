import matplotlib.pyplot as plt
import networkx as nx

# Creating a directed graph
G = nx.DiGraph()

# Defining nodes and their positions
nodes = ["Start", "Erkrankt", "Nicht erkrankt", "Positiv | Erkrankt", "Negativ | Erkrankt", 
         "Positiv | Nicht erkrankt", "Negativ | Nicht erkrankt"]
positions = {"Start": (0, 0), "Erkrankt": (-1, -1), "Nicht erkrankt": (1, -1), 
             "Positiv | Erkrankt": (-2, -2), "Negativ | Erkrankt": (0, -2), 
             "Positiv | Nicht erkrankt": (2, -2), "Negativ | Nicht erkrankt": (0, -3)}

# Adding nodes to the graph
G.add_nodes_from(nodes)

# Adding edges to the graph
G.add_edge("Start", "Erkrankt", weight=0.00110)  # Probability of being ill
G.add_edge("Start", "Nicht erkrankt", weight=0.99890)  # Probability of not being ill
G.add_edge("Erkrankt", "Positiv | Erkrankt", weight=0.9600)  # True positive rate
G.add_edge("Erkrankt", "Negativ | Erkrankt", weight=0.0400)  # False negative rate
G.add_edge("Nicht erkrankt", "Positiv | Nicht erkrankt", weight=0.0220)  # False positive rate
G.add_edge("Nicht erkrankt", "Negativ | Nicht erkrankt", weight=0.9780)  # True negative rate

# Drawing the graph
plt.figure(figsize=(10, 6))
nx.draw(G, pos=positions, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels={(u, v): f"{d['weight']:.5f}" for u, v, d in G.edges(data=True)}, font_color='red')
plt.title("Baumdiagramm: Schnelltest für Darmkarzinome", size=15)
plt.show()
