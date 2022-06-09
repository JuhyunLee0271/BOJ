import sys
input = sys.stdin.readline

N = int(input())
a = list(input().rstrip().split())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if a[i] == a[i+1]:
        dp[i][i+1] = 1
        
for i in range(2, N):
    for j in range(N-i):
        if a[j] == a[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])