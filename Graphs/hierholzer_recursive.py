from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.circuit = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def remEdge(self, u, v):
        for i in self.graph:
            if i == u:
                self.graph[i].remove(v)
        for i in self.graph:
            if i == v:
                self.graph[i].remove(u)

    def printGraph(self):
        for key in self.graph:
            print(key, " -->", self.graph[key])

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    def isConnected(self):
        visited = defaultdict(bool)
        for i in self.graph:
            visited[i] = False
        counter = 0
        for i in self.graph:
            counter += 1
            if len(self.graph[i]) > 1:
                break
        if counter == self.V - 1:
            return True
        self.DFS(i, visited)
        for i in self.graph:
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True

    def isEulerianCircuitExists(self):
        if self.isConnected() == False:
            return False
        else:
            odd = 0
            for i in self.graph:
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
            if odd == 0:
                return True
            else: return False
            
    def returnStart(self):
        return list(self.graph.keys())[0]
            
    def EulerianCircuitfromHeirholzer(self,v):
        for i in self.graph[v]:
            self.remEdge(v,i)
            self.EulerianCircuitfromHeirholzer(i)
        self.circuit.append(v)
        
           
if __name__ == "__main__":
    
    v = int(input("Enter the number of vertices in the graph: "))
    g1 = Graph(v)
    
    max_edges = (v*(v-1))/2
    while True:
        edges = int(input("Number of Edges in your graph: "))
        if edges > max_edges:
            print("Error! Maximum number of Edges in a graph with vertices",
                  v, "can be", max_edges)
            print("Please Enter again: ")
        else:
            break
    
    for i in range(edges):
        print("Enter the ends of edge", i+1)
        li = list(input().split())
        g1.addEdge(li[0], li[1])
    
    g1.printGraph()

    result = g1.isEulerianCircuitExists()
    if result:
        g1.EulerianCircuitfromHeirholzer(g1.returnStart())
        answer = g1.circuit
        print("Euler Circuit: ")
        for k in answer:
            print(k,end=" ")
    
    











