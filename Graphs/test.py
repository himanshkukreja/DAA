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
    
    
    def SearchhamCycle(self,vertex,label,instack_count,stack):
        if instack_count == self.V:
            return True
        for i in self.graph:
            if self.isVertexConnected(vertex,i) and not label[i]:
                label[i]=True
                stack.append(i)
                if self.SearchhamCycle(i,label,instack_count+1,stack):
                    return True
                label[i]=False
                stack.remove(i)
        return False
                
    def getHamiltoniancycles(self):
        if not self.isConnected():
             return False
        else:
             label = defaultdict(bool)
             answer = []
             for vertex in self.graph:
                 label[vertex]=False
             for i in self.graph:
                 stack = []
                 stack.append(i)
                 label[i]=True
                 if self.SearchhamCycle(i,label,1,stack):
                       answer.append(stack)
                       continue
                 label[i]=False
                 stack.remove(i)
             if len(answer):
                 return answer
             return False

if __name__ == "__main__":
    result = []
    t = int(input())
    for j in range(t):
        data =  list (map (int, input().strip().split()))
        v = data[0]
        edges = data[1]
        if edges==0:
            result.append("No")
            continue
	    g = Graph(v)
	    for i in range(edges):
		    li = list (map (int, input().strip().split()))
		    g.addEdge(li[0], li[1])
	    path = g.getHamiltoniancycles()
	    if path == False:
		    result.append("No")
	    else:
	        result.append("Yes")

    for i in result:
	    print(i)
		
