N = int(input())
dp = [0] * 31
dp[1] = 0
dp[2] = 3
dp[3] = 0
dp[4] = 11

for i in range(4, N+1):
    if i % 2 == 0:
        dp[i] = dp[i-2]*3 + sum(dp[:i-2] * 2) + 2
    else:
        dp[i] = 0

print(dp[N])

