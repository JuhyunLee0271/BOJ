from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(arr, x, y):
    q = deque()
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1
    q.append((x,y,1))

    while q:
        x, y, w = q.popleft()
        if x == N-1 and y == M-1:
            return visited[nx][ny][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx,ny,0))
                elif arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx,ny,w))
    return -1

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip())))

print(BFS(arr, 0,0))