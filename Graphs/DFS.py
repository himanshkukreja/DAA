# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:09:48 2021

Find a path from source to destination

@author: Himanshu kukreja
"""

from collections import defaultdict
global paths
paths = []

graph = { 's' : [['v1', 16], ['v2', 13]],
'v1' : [['v3', 12]],
'v3' :  [['t', 20], ['v2', 9]],
'v2' :  [['v4', 14], ['v1', 4]],
'v4' : [['t', 4], ['v3', 7]]
}


def PrintAllPathsUtil(graph,source,destination,visited,path):
    global paths
    visited[source] = True
    path.append(source)
    if source == destination: 
        paths.append(path)
        print(path)
        print(paths)
    
    else:
        for i in graph[source]:
            if not visited[i[0]]:
                PrintAllPathsUtil(graph,i[0],destination,visited,path)
                
    path.pop()
    visited[source] = False
        
def PrintAllPaths(graph,source,destination):
    visited = defaultdict(bool)
    for i in graph:
        visited[i] = False
    path = []
    PrintAllPathsUtil(graph,source,destination,visited,path)


PrintAllPaths(graph,"s","t")
print(paths)