import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = [[0, 0]]
dp = [[0] * (T+1) for _ in range(N+1)]
for _ in range(N):
    K, S = map(int, input().split())
    arr.append([K, S]) # [time, score] 

# knapsack algorithm
for i in range(1, N+1):
    for j in range(1, T+1):
        time, score = arr[i][0], arr[i][1]
        if j < time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + score)

print(dp[N][T])