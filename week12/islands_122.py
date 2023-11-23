#!/usr/bin/env python3

import sys

def bfs(graph, start_vertex, visited):
    queue = [start_vertex]
    visited[start_vertex] = True
    index = 0
    
    while index < len(queue):
        current_vertex = queue[index]
        index += 1
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def find_islands(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    num_islands = 0
    
    for vertex in range(num_vertices):
        if not visited[vertex]:
            bfs(graph, vertex, visited)
            num_islands += 1
    
    return num_islands

if __name__ == '__main__':
    graph = {}
    num_vertices = int(sys.stdin.readline().strip())
    for line in sys.stdin:
        v1, v2 = map(int, line.strip().split())
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(find_islands(graph))