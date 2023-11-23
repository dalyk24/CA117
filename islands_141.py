#!/usr/bin/env python3

import sys

class Graph:
    def __init__(self):
        self.entries = []
        self.adj = {}
        self.visited = {}

    def addentry(self, v):
        self.entries.append(v)
        self.adj[v] = []
        self.visited[v] = False

    def addedge(self, v, w):
        self.adj[v].append(w)

    def dfspaths(self):
        islands = 0

        for v in self.entries:
            if self.visited[v] == False:
                islands += 1
                self.dfs(v)

        return islands

    def dfs(self, v):
        self.visited[v] = True

        for w in self.adj[v]:
            if not self.visited[w]:
                self.dfs(w)

letters = [l.strip() for l in sys.stdin.readlines()]

g = Graph()
counter = 0

for i, line in enumerate(letters):
    for j, l in enumerate(line):
        if l == "L":
            temp = l + str(counter)
            g.addentry(temp)
            if j > 0 and line[j-1] == "L":
                g.addedge(temp, line[j-1] + str(counter-1))
            if j < len(line) - 1 and line[j+1] == "L":
                g.addedge(temp, line[j+1] + str(counter+1))
            if i > 0 and letters[i-1][j] == "L":
                g.addedge(temp, letters[i-1][j] + str(counter-len(line)))
            if i < len(letters) - 1 and letters[i+1][j] == "L":
                g.addedge(temp, letters[i+1][j] + str(counter+len(line)))
        counter += 1

print(g.dfspaths())
