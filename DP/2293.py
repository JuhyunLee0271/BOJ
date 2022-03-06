N,K = map(int, input().split())
dp = [0]*(K+1)
coins = []
for _ in range(N):
    coins.append(int(input()))
dp[0] = 1

for i in coins:
    for j in range(1, K+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[K])

