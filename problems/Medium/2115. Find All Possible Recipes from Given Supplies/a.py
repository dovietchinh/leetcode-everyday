import networkx as nx
import matplotlib.pyplot as plt 
a = ["zpmcz","d","ju","cpivl","e","h","fzjnm","hveml","f","q","x"]



data =  {
    'ju': ['d'],
    'fzjnm':['hveml', 'f', 'cpivl'],
    'x': ['cpivl', 'zpmcz', 'h', 'e', 'fzjnm', 'ju'],
    'e': ['cpivl', 'hveml', 'zpmcz', 'ju', 'h'],
    'zpmcz': ['h', 'fzjnm', 'e', 'q', 'x'],
    'h': ['d', 'hveml', 'cpivl', 'q', 'zpmcz', 'ju', 'e', 'x'],
    'q': ['f', 'hveml', 'cpivl']
    }
j = {}
# ["f","hveml","cpivl","d"]
edges = []
for k,v in data.items():
    for v1 in v:
        if a.index(k) == -1 or a.index(v1) == -1:
            continue 
        edges.append((a.index(k),a.index(v1)))

print('edges: ',edges)  

G = nx.MultiDiGraph()

G.add_edges_from(edges)

# plt.figure(figsize=(8,8))
pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True, node_color='lightblue',)

plt.show()


