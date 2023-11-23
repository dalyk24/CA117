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

class DFSPaths(object):
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True

        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        self.dfs(self.s)
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
             return []

        path = [v]
        while v != self.s and self.parent[v] != -1:
            v = self.parent[v]
            path.append(v)

        return path[::-1]

import sys

from graph_dfs_112 import Graph, DFSPaths

def main():

    with open('graph_input_00_112.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    dfs = DFSPaths(g, 4)
    print(dfs.hasPathTo(2))
    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()
