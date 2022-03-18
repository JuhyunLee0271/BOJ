from collections import deque

def BFS(vertex):
    q = deque()
    q.append(vertex)
    visited[vertex] = True
    cnt = -1

    while q:
        v = q.popleft()
        for e in arr[v]:
            if visited[e] == False:
                visited[e] = True
                q.append(e)
                cnt += 1
    return cnt

N,M = map(int, input().split())
arr = []    
cnt = 0
visited = [False] * (N+1)

for i in range(N+1):
    arr.append([])
for i in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for i in range(1, N+1):
    result = BFS(i)
    if result != -1:
        cnt += 1

print(cnt)



