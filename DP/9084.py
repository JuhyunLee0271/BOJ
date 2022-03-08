import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target+1)
    dp[0] = 1

    for i in coins:
        for j in range(1, target+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
                
    print(dp[target])



