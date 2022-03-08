import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [[100000] * (3) for i in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp[0] = arr[0].copy()

for i in range(1, N):
    for j in range(3):
        if j == 0: dp[i][j] = min(dp[i-1][j+1], dp[i-1][j+2]) + arr[i][j]
        elif j == 2: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + arr[i][j]
        else: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]) + arr[i][j]

print(min(dp[N-1]))

