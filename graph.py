


class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    
c = {
    "a": ["b","c","d"],
    "b": ["a","e"],
    "c": ["a","d"],
    "d": ["a","c"],
    "e": ["b","d"]
}

graph = Graph(c)
graph.addEdge("d","e")
print(graph.gdict["d"])