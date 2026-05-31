class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item
            self.current = self.current.next
            return item


class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return "%d->%s %.5f" % (self.v, self.w, self.weight)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def From(self):
        return self.v

    def To(self):
        return self.w

class EdgeWeightedDigraph:
    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

        if 'file' in kwargs:
            # init a digraph by a file input
            in_file = kwargs['file']
            self.V = int(in_file.readline())
            self.adj = [Bag() for _ in range(self.V)]
            E = int(in_file.readline())
            for i in range(E):
                v, w, weight = in_file.readline().split()
                self.add_edge(DirectedEdge(int(v), int(w), float(weight)))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for i in range(self.V):
            adjs = " ".join([str(x) for x in self.adj[i]])
            s += "%d: %s\n" % (i, adjs)
        return s

    def add_edge(self, e):
        self.adj[e.From()].add(e)
        self.E += 1

    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                edges.append(e)
        return edges


import heapq

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

