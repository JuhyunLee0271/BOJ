from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif graph[nx][ny] == 0:
                    counts[x][y] += 1
    return 1

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

flag = False
day = 0
while True:
    temp = []
    visited = [[False]*M for _ in range(N)]
    counts = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                temp.append(BFS(i,j))
    
    for i in range(N):
        for j in range(M):
            graph[i][j] = max(0, graph[i][j] - counts[i][j])
    
    if len(temp) == 0:
        break
    elif len(temp) >= 2:
        flag = True
        break
    day += 1

if flag: print(day)
else: print(0)
