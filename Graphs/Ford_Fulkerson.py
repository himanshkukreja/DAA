# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:00:07 2021

Identify the Maximum Flow in a given network

@author: Himanshu kukreja
"""

from collections import defaultdict
import copy
class FlowNetwork:

    def __init__(self,vertices,source,sink):
        self.V = vertices
        self.graph = defaultdict(list)
        self.flow = 0
        self.source = source
        self.sink = sink
        self.paths = []

    def addEdge(self,u,v,wt):
        self.graph[u].append([v,wt,0])
        

    def printGraph(self):
        for key in self.graph:
            print(key," -->",self.graph[key])
            
    def DFS(self,v,visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i[0]] == False:
                self.DFS(i[0],visited)
    
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
    
    def SearchPathsUtil(self,graph,s,t,visited,path):
        visited[s] = True
        path.append(s)
        if s==t:
            print(path)
            self.paths.append(path)
        else:
            for i in graph[s]:
                if not visited[i[0]]:
                    self.SearchPathsUtil(graph,i[0],t,visited,path)
        path.pop()
        visited[s] = False
        

    def SearchPath(self,residualGraph):
        visited = defaultdict(bool)
        for i in self.graph:
            visited[i] = False
        path=[]
        self.SearchPathsUtil(residualGraph,self.source,self.sink,visited,path)
        return self.paths
        

    def FordFulkerson(self):
        residualGraph = copy.deepcopy(self.graph)
        print(self.SearchPath(residualGraph))
        
        

g = FlowNetwork(6,"s","t")
g.addEdge("s","v1",16)
g.addEdge("v1","v3",12)
g.addEdge("v3","t",20)
g.addEdge("s","v2",13)
g.addEdge("v2","v4",14)
g.addEdge("v4","t",4)
g.addEdge("v2","v1",4)
g.addEdge("v3","v2",9)
g.addEdge("v4","v3",7)

g.printGraph()
g.FordFulkerson()
