from collections import deque
import sys
input = sys.stdin.readline

dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
def BFS():
    visited[sx][sy][sz] = 0
    q = deque()
    q.append((sx, sy, sz))
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if visited[nx][ny][nz] == -1 and arr[nx][ny][nz] != '#':
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx, ny, nz))
    
    ex, ey, ez = 0, 0, 0
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'E':
                    ex, ey, ez = i, j, k

    if visited[ex][ey][ez] == -1:
        return "Trapped!"
    else:
        return F"Escaped in {visited[ex][ey][ez]} minute(s)."

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    arr = [[] * R for _ in range(L)]
    for i in range(L):
        for j in range(R):
            arr[i].append(list(map(str, input())))
        input()
    
    visited = [[[-1] * (C) for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    sx, sy, sz = i, j, k
                elif arr[i][j][k] == 'E':
                    ex, ey, ez = i, j, k    
    print(BFS())
