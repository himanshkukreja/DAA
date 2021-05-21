# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:11:35 2021

Search a path in Graph using BFS

@author: Himanshu kukreja
"""

from collections import defaultdict

graph = { 's' : [['v1', 16], ['v2', 13]],
'v1' : [['v3', 12]],
'v3' :  [['t', 20], ['v2', 9]],
'v2' :  [['v4', 14], ['v1', 4]],
'v4' : [['t', 4], ['v3', 7]]
}

global paths 
paths = []

def isVertexVisited(x,path):
    for i in path:
        if i==x:
            return True
        else: return False

def BFS(graph,source,destination):
    queue = []
    path=[]
    path.append(source)
    queue.append(path)
    while queue:
        path = queue.pop(0)
        print(path)
        last = path[len(path)-1]
        print(last)
        if last == destination:
            print(path)
            paths.append(path)
        for i in range(len(graph[last])):
            if graph[last][i][0] not in path:
                newpath = path.copy()
                newpath.append(graph[last][i][0])
                queue.append(newpath)


BFS(graph,"s","t")

            
        
    