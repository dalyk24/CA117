#!/usr/bin/env python3

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.adj = {}

        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max([self.degree(v) for v in self.adj])

    def avgDegree(self):
        return sum([self.degree(v) for v in self.adj]) / self.V

class BFSPaths(object):
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
        self.queue = []
        self.queue.append(s)
        self.visited[s] = True

        while self.queue:
            v = self.queue.pop(0)

            for w in self.g.adj[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    self.parent[w] = v
                    self.queue.append(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
             return []

        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)

        return path[::-1]

import sys

def main():

    with open('input_01.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    bfs = BFSPaths(g, 4)
    print(bfs.hasPathTo(2))
    print(bfs.pathTo(2))

if __name__ == '__main__':
    main()
