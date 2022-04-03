from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    
    return cnt    
    
N, M, K = map(int, input().split())
graph = [[[] for _ in range(M)] for _ in range(N)]
visited = [[False] * M for _ in range(N)]

result = []

for _ in range(K):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            result.append(BFS(i, j))

print(max(result))
    