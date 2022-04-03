from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    global sheep
    global wolf
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    a, b = 0, 0
    if graph[x][y] == 'o': a += 1
    elif graph[x][y] == 'v': b += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if graph[nx][ny] != '#':
                    if graph[nx][ny] == 'o': a += 1
                    elif graph[nx][ny] == 'v': b += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    if a > b: sheep += a
    elif a <= b: wolf += b

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
sheep, wolf = 0, 0

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visited[i][j]:
            BFS(i, j)

print(sheep, wolf)