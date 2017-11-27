# -*- coding:utf-8 -*-
import heapq
G = [
    {1:28,5:10},         #0
    {0:28,2:16,6:14},    #1
    {1:16,3:12},         #2
    {2:12,4:22,6:18},    #3
    {3:22,5:25,6:24},    #4
    {0:10,4:25},         #5
    {1:14,3:18,4:24}     #6
]
def prim(G,v):
    n = len(G)
    visited = [v]
    edges = []
    res = []
    for _ in range(n-1):
        for next_v, weight in G[v].iteritems():          #错误一：将iteritems写成了iteriterms
            heapq.heappush(edges,(weight,v,next_v))      #错误二：压栈和解包时，格式一致，(w,v,next_v)--> w,v,next_v = heappop(edges)
        while edges:
            weight,v,next_v = heapq.heappop(edges)       #错误三：heappop()括号里需要传入参数
            if next_v not in visited:
                visited.append(next_v)
                res.append((weight,(v,next_v)))
                v = next_v
                break                                    #错误四：未写break
    return res

res = prim(G,1)
print res