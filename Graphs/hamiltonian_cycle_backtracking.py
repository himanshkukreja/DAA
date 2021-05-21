# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:30:32 2021

Identify the Hamiltonian Cycle using BackTracking

@author: Himanshu kukreja
"""
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
    
    def isSafe(self,v,position,path):
        if self.isVertexConnected(path[position-1],v) and (v not in path):
            return True
        else: return False 
        
    
    def hamCycle(self,path,position):
        if position == self.V:
            if self.isVertexConnected(path[position-1],path[0]):
                return True
            else: return False
            
        for i in range(1,self.V):
            if self.isSafe(i,position,path):
                path[position]=i
                if self.hamCycle(path,position+1):
                    return True
                path[position]=-1
                
        return False
                
    
    def getHamiltoniancycles(self):
        if not self.isConnected():
             return self.Hamcycles
        else:
            path=[-1]*self.V
            path[0] = 0
            
            if not self.hamCycle(path,1):
                return False
            
            else: 
                return path
            

if __name__ == "__main__":
    
    g3 = Graph (4)
    g3.addEdge(1, 2)
    g3.addEdge(2, 3)
    g3.addEdge(3, 0)
    g3.addEdge(0, 1)
    g3.addEdge(1, 3)
    g3.printGraph()
    
    path = g3.getHamiltoniancycles()
    if path == False:
        print("No Hamiltonion Cycle Exists")
    else:
        print("Hamiltonian path:")
        for i in path:
            print(i,end=" ")
    
