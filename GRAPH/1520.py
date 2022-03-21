import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def DFS(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == M-1 and y == N-1:
        return 1

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and arr[x][y] > arr[nx][ny]:
            dp[x][y] += DFS(nx, ny)
    
    return dp[x][y]

M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
dp = [[-1] * N for _ in range(M)]

print(DFS(0,0))

for i in range(M):
    for j in range(N):
        print(dp[i][j], end=' ')
    print()