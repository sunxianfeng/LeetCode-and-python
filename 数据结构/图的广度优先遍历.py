# -*- coding:utf-8 -*-
G = [
    {1,2,3}, #0
    {0,4}, #1
    {0,3},   #2
    {0,2,4}, #3
    {1,3,5},#4
    {2,4},    #5
]
def bfs(G,v):
    q = [v]
    visited = {v}
    while q:
        u = q.pop(0)
        print u
        for w in G[u]:
            if w not in visited:
                q.append(w)
                visited.add(w)
bfs(G,0)
    

