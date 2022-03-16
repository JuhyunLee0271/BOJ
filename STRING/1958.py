import sys
input = sys.stdin.readline

A = [0] + list(input().rstrip())
B = [0] + list(input().rstrip())
C = [0] + list(input().rstrip())

dp = [[[0] * (len(C)) for i in range(len(B))] for j in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        for k in range(1, len(C)):
            if A[i] == B[j] == C[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

print(dp[-1][-1][-1])
