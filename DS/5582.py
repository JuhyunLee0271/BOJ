import sys
input = sys.stdin.readline
S = [''] + list(input().rstrip())
T = [''] + list(input().rstrip())

len_s = len(S)
len_t = len(T)

dp = [[0] * (len_s) for i in range(len_t)]
answer = 0
for i in range(1, len_t):
    for j in range(1, len_s):
        if S[j] == T[i]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)
