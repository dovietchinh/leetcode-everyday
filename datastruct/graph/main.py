class AdjacencyMatrixGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight  # For an undirected graph

    def print_matrix(self):
        print('-------------------------AdjacencyMatrixGraph-------------------------')
        for row in self.adj_matrix:
            print(row)

# Example usage
g_matrix = AdjacencyMatrixGraph(4)
g_matrix.add_edge(0, 1)
g_matrix.add_edge(0, 2)
g_matrix.add_edge(1, 2)
g_matrix.print_matrix()


class AdjacencyListGraph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # For an undirected graph

    def print_list(self):
        print('-------------------------AdjacencyListGraph-------------------------')
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

# Example usage
g_list = AdjacencyListGraph()
g_list.add_edge(0, 1)
g_list.add_edge(0, 2)
g_list.add_edge(1, 2)
g_list.print_list()



class EdgeListGraph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight=1):
        self.edges.append((u, v, weight))

    def print_edges(self):
        print('-------------------------EdgeListGraph----------------')
        for edge in self.edges:
            print(edge)

# Example usage
g_edge = EdgeListGraph()
g_edge.add_edge(0, 1)
g_edge.add_edge(0, 2)
g_edge.add_edge(1, 2)
g_edge.print_edges()

class IncidenceMatrixGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.inc_matrix = []

    def add_edge(self, u, v):
        self.edges.append((u, v))
        self.update_incidence_matrix()

    def update_incidence_matrix(self):
        self.inc_matrix = [[0] * len(self.edges) for _ in range(self.V)]
        for i, (u, v) in enumerate(self.edges):
            self.inc_matrix[u][i] = 1
            self.inc_matrix[v][i] = 1

    def print_incidence_matrix(self):
        print('-------------------------IncidenceMatrixGraph-------------------------')
        for row in self.inc_matrix:
            print(row)

# Example usage
g_incidence = IncidenceMatrixGraph(3)
g_incidence.add_edge(0, 1)
g_incidence.add_edge(1, 2)
g_incidence.print_incidence_matrix()