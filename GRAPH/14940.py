from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            dist[i][j] = -1
        if graph[i][j] == 2:
            start = [i, j]
            
dx, dy = [0,0,-1,1], [-1,1,0,0]
q = deque()
q.append(start)
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])

for i in range(N):
    for j in range(M):
        print(dist[i][j], end=' ')
    print()
            
                
