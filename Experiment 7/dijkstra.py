class Graph:
    dist = []
    prev = []

    def __init__(self, edges):
        self.edges = edges
        self.vertices = set(range(0, edges))
        self.matrix = [[0]*edges]*edges

    def input_vertices(self):
        source = int(input("Enter the source: "))
        dest = int(input("Enter the destination: "))
        weight = int(input("Enter the weight: "))
        self.matrix[source-1][dest-1] = weight

    def dijkstra(self, source):
        self.dist[source] = 0
        for v in self.vertices:
            if v != source:
                self.dist[v] = 999
                self.prev[v] = "undefined"


graph = Graph(9)
graph.input_vertices()
graph.dijkstra(0)



