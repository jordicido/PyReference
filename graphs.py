class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if self.graph.get(u) == None:
            self.graph[u] = []
            
        if self.graph.get(v) == None:
            self.graph[v] = []
            
        self.graph[v].append(u)
        self.graph[u].append(v)
        
    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) or (u in self.graph[v])
        return False


def test(edges_to_add, edges_to_test):
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("-------------------------------------")
    for edge in edges_to_test:
        exists = graph.edge_exists(edge[0], edge[1])
        print(f"{edge} exists: {exists}")
    print("=====================================")


def main():
    test(
        [
            (0, 1),
            (2, 0),
        ],
        [
            (1, 0),
            (1, 2),
            (2, 0),
        ],
    )
    test(
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        [
            (0, 1),
            (1, 2),
            (0, 4),
            (2, 5),
            (5, 0),
        ],
    )


main()
