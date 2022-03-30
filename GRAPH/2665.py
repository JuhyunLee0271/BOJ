from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
    
    return visited[-1][-1]

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

print(BFS(0, 0))