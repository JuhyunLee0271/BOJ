import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

# K = 2일 때, 0 ~ N의 수로 N을 만드는 가지수는 N+1
if K == 1:
    print(1)
else:
    for i in range(0, N+1):
        dp[i][2] = i+1

    for k in range(3, K+1):
        for i in range(0, N+1):
            for j in range(0, i+1):
                dp[i][k] = (dp[i][k] + dp[j][k-1])%1000000000

    print(dp[-1][-1]%1000000000)