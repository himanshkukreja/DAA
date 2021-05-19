from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for key in self.graph:
            print(key," -->",self.graph[key])
            
    def DFS(self,v,visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i,visited)
    
    def isConnected(self):
        visited = defaultdict(bool)
        for i in self.graph:
            visited[i] = False
        counter = 0
        for i in self.graph:
            counter += 1
            if len(self.graph[i])>1:
                break
        if counter == self.V - 1:
            return True
        self.DFS(i,visited)
        for i in self.graph:
            if visited[i] == False and len(self.graph[i])>0:
                return False
        return True


    def isEulerian(self):
        if self.isConnected()==False:
            print("The Graph is not connected, Hence it can not be Eulerian")
            return
        else:
            odd = 0
            for i in self.graph:
                if len(self.graph[i])%2 != 0:
                    odd += 1
            if odd == 0:
                print("Graph is Eulerian")
            elif odd == 2:
                print("Graph is Semi Eulerian")
            else:
                print("Graph is not Eulerian")
        return
            


v = int(input("Enter the number of vertices in the graph: "))
g1 = Graph(v)

max_edges = (v*(v-1))/2
while True:
    edges = int(input("Number of Edges in your graph: "))
    if edges>max_edges:
        print("Error! Maximum number of Edges in a graph with vertices",v,"can be",max_edges)
        print("Please Enter again: ")
    else: break

for i in range(edges):
    print("Enter the ends of edge",i+1)
    li = list(input().split())
    g1.addEdge(li[0], li[1])

g1.printGraph()
g1.isEulerian()





# if g1.isConnected():
#     print("Your Graph is connected")

# g1 = Graph(5)
# g1.addEdge(1, 0)
# g1.addEdge(0, 2)
# g1.addEdge(2, 1)
# g1.addEdge(0, 3)
# g1.addEdge(3, 4)
    
# g1.printGraph()
# print(g1.isConnected())