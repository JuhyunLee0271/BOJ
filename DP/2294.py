import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [100001] * 100001
coins = []
for _ in range(N):
    coins.append(int(input()))

for c in coins:
    dp[c] = 1

for i in range(1, K+1):
    for j in coins:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + 1)

print(-1) if dp[K] == 100001 else print(dp[K])