import heapq
from directed_edge import DirectedEdge
from edge_weighted_digraph import EdgeWeightedDigraph

s = int(input())
    
for _ in range(s):
    n = int(input())
    city_index = {}
    graph = EdgeWeightedDigraph(n)
    
    for i in range(n):
        city = input()
        city_index[city] = i
        p = int(input())
        for _ in range(p):
            nb,cost = map(int, input().split())
            nb = nb - 1
            graph.add_edge(DirectedEdge(i, nb, cost))
    
    r = int(input())
    for _ in range(r):
        src = input()
        dst = input()
        s_id, d_id = city_index[src], city_index[dst]
        INF = 10**12
        dist = [INF] * n
        dist[s_id] = 0
        pq = [(0, s_id)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == d_id:
                break
            for edge in graph.adj[u]:
                v = edge.To()
                w = edge.Weight()
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        print(dist[d_id])