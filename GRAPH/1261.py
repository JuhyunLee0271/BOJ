from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    q = deque()
    q.append((x, y))
    
    cost = [[-1]*M for _ in range(N)]
    cost[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if cost[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        cost[nx][ny] = cost[x][y]
                        q.appendleft((nx, ny))
                    elif graph[nx][ny] == 1:
                        cost[nx][ny] = cost[x][y] + 1
                        q.append((nx, ny))
    
    print(cost[N-1][M-1])

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

BFS(0,0)
