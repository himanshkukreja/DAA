from collections import defaultdict
import time

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.HamCycles = []

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

    def isVertexConnected(self, u, v):
        connected = False
        for i in self.graph[u]:
            if i == v:
                connected = True
                break
        return connected

    def permutations(self, li):
        if len(li) == 0:
            return []
        if len(li) == 1:
            return [li]
        per = []

        for i in range(len(li)):
            m = li[i]
            remList = li[:i] + li[i+1:]

            for p in self.permutations(remList):
                per.append([m] + p)
        return per

    def getHamiltoniancycles(self):
        if not self.isConnected():
            return self.Hamcycles
        else:
            vertices = list(self.graph.keys())
            permutations = self.permutations(vertices)
            Possibilities = []
            for p in permutations:
                validP = True
                for i in range(len(p)-1):
                    if not self.isVertexConnected(p[i], p[i+1]):
                        validP = False
                        break
                if validP == True:
                    Possibilities.append(p)
            for j in Possibilities:
                if self.isVertexConnected(j[0], j[-1]):
                    self.HamCycles.append(j)
        return self.HamCycles


if __name__ == "__main__":
    
    time1 = time.time()

    '''
    g3 = Graph (4)
    g3.addEdge(1, 2)
    g3.addEdge(2, 3)
    g3.addEdge(3, 0)
    g3.addEdge(0, 1)
    g3.addEdge(1, 3)
    '''
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
    cycles = g1.getHamiltoniancycles()
    if cycles:
        print("Hamiltonian Cycles are:")
        for cycle in cycles:
            for i in cycle:
                print(i, end=" ")
            print()

    else:
        print("No Hamiltonian Cycles Exists")

    time2 = time.time()
    print("Time Taken for code to execute",time2-time1,"milliseconds")