import sys
input = sys.stdin.readline

M = input().rstrip()
N = input().rstrip()

dp = [[""] * (len(M)+1) for _ in range(len(N)+1)]

for i in range(1, len(N)+1):
    for j in range(1, len(M)+1):
        if M[j-1] == N[i-1]:
            dp[i][j] = dp[i-1][j-1] + M[j-1]
        else:
            a, b, c = len(dp[i-1][j-1]), len(dp[i-1][j]), len(dp[i][j-1])
            if max(a, b, c) == a:
                dp[i][j] = dp[i-1][j-1]
            elif max(a, b, c) == b:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

result = dp[-1][-1]
print(len(result))
print(result)