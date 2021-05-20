from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.HamCycles=[]

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
    
    def Binary(self,n):
        binary =  bin(n).replace("0b", "")
        size = len(binary)
        diff = self.V - size
        if diff:
            binary = "0"*diff + binary
        return binary
            
        
    
    def HamDyanimicProgramming(self):
        n = self.V
        A = []
        P=[]
        for i in range(2**n):
            col = []
            for j in range(n):
                col.append("__")
            A.append(col)
            
        for i in range(2**n):
            col = []
            for j in range(n):
                col.append("__")
            P.append(col)
        
        for i in range(2**n):
            Bitmask = self.Binary(i)
            rev_Bitmask = Bitmask[::-1]
            for j in range(n):
                if rev_Bitmask[j]=="0":
                    A[i][j] = 0
                    P[i][j] = 0
        
        for i in range(n):
            A[2**i][i] = 1
            if self.isVertexConnected(i,0):
                P[2**i][i] = 0
            else:
                P[2**i][i] = "phi"
        print(A)
        print(P)
        
        for j in range(2**n):
            if "__" in A[j]:
                for i in range(n):
                    if A[j][i]=="__":
                        k_list=[]
                        for k in range(n):
                            if A[j][k]=="__" and not(k == i) and self.isVertexConnected(i,k):
                                k_list = k_list+[k]
                        print(f"A[{j}][{i}] k_list: {k_list}")
                        if not len(k_list):
                            A[j][i]=0
                        else:
                            for k in k_list:
                                XOR = j^(2**i)
                                print(f"A[{j}][{i}] XOR : {XOR}")
                                if A[XOR][k]:
                                    A[j][i]=1
                                    print(f"A[{j}][{i}] = 1")
                                    P[j][i]=k
                                    print(f"P[{j}][{i}] = {k}")
                                else: 
                                    A[j][i]=0
                                    P[j][i]="phi"
        
        print(A)
        print(P)          
                    
                
        
g3 = Graph (4)
g3.addEdge(1, 2)
g3.addEdge(2, 3)
g3.addEdge(3, 1)
g3.addEdge(0, 1)
g3.printGraph()
g3.HamDyanimicProgramming()

    
