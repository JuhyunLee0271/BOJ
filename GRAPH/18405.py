from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

temp = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            temp.append((arr[i][j], i, j, 0))
            
temp.sort()
q = deque(temp)

dx, dy = [-1,1,0,0], [0,0,-1,1]
while q:
    level, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = level
            q.append((level, nx, ny, time + 1))

print(arr[X-1][Y-1])