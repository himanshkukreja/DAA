from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

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

    def isEulerian(self):
        if self.isConnected() == False:
            return (False, -1)
        else:
            odd = 0
            for i in self.graph:
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
            if odd == 0:

                return (True, 1)
            elif odd == 2:

                return (True, 2)
            else:

                return (False, 0)

    def remEdge(self, u, v):
        for i in self.graph:
            if i == u:
                self.graph[i].remove(v)
        for i in self.graph:
            if i == v:
                self.graph[i].remove(u)

    def DFScount(self, vertex, visited):
        count = 1
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                count = count + self.DFScount(i, visited)
        return count

    def isValidNext(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        else:
            visited = defaultdict(bool)
            for i in self.graph:
                visited[i] = False
            count1 = self.DFScount(u, visited)

            self.remEdge(u, v)

            visited = defaultdict(bool)
            for i in self.graph:
                visited[i] = False
            count2 = self.DFScount(u, visited)

            self.addEdge(u, v)

            if count1 > count2:
                return False
            else:
                return True

    def printEulerUtil(self, u):
        for v in self.graph[u]:
            if self.isValidNext(u, v):
                print(f"{v}", end=' ')
                self.remEdge(u, v)
                self.printEulerUtil(v)

    def printEulerTour(self):
        u = list(self.graph.keys())[0]
        for i in self.graph:
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        print(f"{u}", end=' ')
        self.printEulerUtil(u)


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
result = g1.isEulerian()

if not result[0]:
    print("Graph is not Eulerian")
else:
    if result[1] == 1:
        print("Graph is Eulerian")
        print("Eulerian Cycle:- ")
        g1.printEulerTour()
    else:
        print("Graph is Semi Eulerian")
        print("Eulerian path:- ")
        g1.printEulerTour()

# g3 = Graph (5)
# g3.addEdge(1, 0)
# g3.addEdge(0, 2)
# g3.addEdge(2, 1)
# g3.addEdge(0, 3)
# g3.addEdge(3, 4)
# g3.addEdge(3, 2)
# g3.addEdge(3, 1)
# g3.addEdge(2, 4)
# g3.printGraph()
