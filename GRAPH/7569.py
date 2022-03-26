from collections import deque
import sys
input = sys.stdin.readline

dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
def BFS(arr, tomatoes):
    q = deque()
    visited = [[[False]*M for _ in range(N)] for _ in range(H)]
    
    for x, y, z in tomatoes:
        q.append((x, y, z))
        visited[x][y][z] = True
    
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if not visited[nx][ny][nz] and arr[nx][ny][nz] != -1:
                    arr[nx][ny][nz] = arr[x][y][z] + 1
                    visited[nx][ny][nz] = True
                    q.append((nx, ny, nz))
    
    cnt = 0
    max_val = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                max_val = max(max_val, arr[i][j][k])
                if arr[i][j][k] == 0:
                    cnt += 1
                
    if cnt > 0: return -1
    else: return max_val - 1

M, N, H = map(int, input().split())
arr = [[]*H for _ in range(H)] 

for i in range(H):
    for _ in range(N):
        arr[i].append(list(map(int, input().split())))

tomatoes = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                tomatoes.append((i,j,k))

print(BFS(arr, tomatoes))