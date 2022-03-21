from collections import deque
import sys
input = sys.stdin.readline

dx,dy = [-1,1,0,0], [0,0,-1,1]
def BFS(targetX, targetY):
    while queue:
        x, y = queue.popleft()
        if graph[targetX][targetY] == 'S':
            return dist[targetX][targetY]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[x][y] == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'S'):
                    graph[nx][ny] = '*'
                    queue.append((nx, ny))
                elif graph[x][y] == 'S' and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                    graph[nx][ny] = 'S'
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    
    return "KAKTUS"

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

queue = deque()
dist = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            queue.appendleft((i,j))
        elif graph[i][j] == '*':
            queue.append((i,j))
        elif graph[i][j] == 'D':
            targetX, targetY = i,j

print(BFS(targetX, targetY))