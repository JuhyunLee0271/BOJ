import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx, dy = [-1,1,0,0], [0,0,-1,1]
def DFS(x, y):
    if dp[x][y] > 0: return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1)
    return dp[x][y]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        result = max(result, DFS(i, j))
print(result)