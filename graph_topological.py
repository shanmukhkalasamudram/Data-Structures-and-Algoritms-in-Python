


from collections import defaultdict

class Graph:
    def __init__(self,numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def edge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
            
        stack.insert(0,v)

    def topologicalSort(self):
        visited = []

        stack = []
 
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)

        print(stack)

a = Graph(8)

a.edge("A","C")
a.edge("C","E")
a.edge("E","H")
a.edge("E","F")
a.edge("F","G")
a.edge("B","D")
a.edge("B","C")
a.edge("D","F")

a.topologicalSort()





