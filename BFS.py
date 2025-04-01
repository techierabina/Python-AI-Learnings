from collections import deque

def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)

    print("BFS Traversial: ",end=" ")
    while queue:
        node=queue.popleft()
        print(node,end=" ")
    
        for neighbor in graph[node]:
          if neighbor not in visited:
              visited.add(neighbor)
              queue.append(neighbor)


graph={
    'A': ['B', 'C'],
    'B':  ['A', 'D','E'],
    'C':  ['A', 'F'],
    'D':  ['E', 'B'],
    'E':  ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph,'A')
bfs(graph,'B')