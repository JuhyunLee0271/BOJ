from collections import deque
import sys
input = sys.stdin.readline

dx,dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    flag = False
    q = deque()
    q.append((x, y))
    
    union = []
    union.append((x, y))
    
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    q.append((nx, ny))
                    union.append((nx, ny))
                    visited[nx][ny] = True
    
    if len(union) >= 2:
        people = sum([graph[x][y] for x, y in union]) // len(union)
        for x, y in union:
            graph[x][y] = people
        flag = True
    return flag

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = 0

while True:
    cond = []
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cond.append(BFS(i,j))
    if True not in cond:
        break
    result += 1

print(result)