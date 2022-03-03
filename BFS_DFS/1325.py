from collections import deque
n, m = map(int, input().split())
arr = []
result = []

def BFS(visited, vertex):
    q = deque()
    q.append(vertex)
    visited[vertex] = True
    
    while q:
        v = q.popleft()
        for e in arr[v]:
            if visited[e] == False:
                visited[e] = True
                q.append(e)

for i in range(n+1):
    arr.append([])
for i in range(m):
    a,b = map(int, input().split())
    arr[b].append(a)

for i in range(1, n+1):
    visited = [False] * (n+1)
    BFS(visited, i)
    result.append(visited.count(True))

for i in range(len(result)):
    if result[i] == max(result):
        print(i+1, end=' ')
