from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    dist = [[-1]*N for _ in range(M)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    
    result = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 'L' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    result = max(result, dist[nx][ny])
                    q.append((nx, ny))

    return result

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(input().rstrip()))

result = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'L':
            result = max(result, BFS(i,j))
print(result)