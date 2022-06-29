from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(hx, hy, ex, ey):
    
    q = deque([[hx, hy, 1]])
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[hx][hy][1] = 0
    
    while q:
        x, y, w = q.popleft()
        if x == ex and y == ey:
            return visited[ex][ey][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][w] + 1
                    q.append([nx, ny, 0])
                elif arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1

N, M = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

print(BFS(hx-1, hy-1, ex-1, ey-1))