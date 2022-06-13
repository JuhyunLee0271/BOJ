import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

dp = [[0] * (len(S)+1) for _ in range(len(T)+1)]

for i in range(1, len(S)+1):
    dp[0][i] = i

for i in range(1, len(T)+1):
    dp[i][0] = i

for i in range(1, len(T)+1):
    for j in range(1, len(S)+1):
        if S[j-1] == T[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[-1][-1])
        
        