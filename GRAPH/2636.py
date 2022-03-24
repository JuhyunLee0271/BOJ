from collections import deque
import sys
input = sys.stdin.readline

dx,dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited = [[False] * N for _ in range(M)]
    visited[x][y] = True
    cheeses = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cheeses.append((nx, ny))
    
    for cx, cy in cheeses:
        graph[cx][cy] = 0
    
    result = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                result += 1
    return result

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

temp = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            temp += 1

result = []
result.append(temp)

while True:
    res = BFS(0,0)
    if res == 0:
        break
    result.append(res)

print(len(result))
print(result[-1])
