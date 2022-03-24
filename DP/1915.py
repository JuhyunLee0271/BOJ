import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip())))

dp = [[0] * (M+1) for _ in range(N+1)]

side = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

print(max(map(max, dp))**2)