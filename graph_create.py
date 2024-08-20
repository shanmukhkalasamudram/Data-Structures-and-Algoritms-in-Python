
from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def addEdge(self,vertex1,vertex2):

        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
        #    current_vertex = queue.pop(0)   -> O(n) So use dequeue in Collections 
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if(adjacent_vertex  not in visited):
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    # O(V+E)

    def dfs(self,vertex):
        visited = set()
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
                
        



custom = Graph()
custom.add_vertex("A")
custom.add_vertex("B")
custom.add_vertex("C")
custom.add_vertex("D")
custom.add_vertex("E")
custom.addEdge("A","B")
custom.addEdge("A","C")
custom.addEdge("B","E")
custom.addEdge("C","D")
custom.addEdge("D","E")
# custom.addEdge("A","B")
# custom.remove_vertex("A")
custom.print_graph()
custom.bfs("A")
custom.dfs("A")

    

