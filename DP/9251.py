s1 = list(input())
s2 = list(input())

N = len(s1)
M = len(s2)

dp = [[0] * (N+1) for i in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):      
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
print(dp[M][N])