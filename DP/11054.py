import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(2)]
dp[0][1] = dp[1][N] = 1

for i in range(2, N+1):
    flag = i
    value = 0
    for j in range(i):
        if numbers[i] > numbers[j] and dp[0][j] > value:
            flag = j
            value = dp[0][j]
    if flag == i:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][flag] + 1

for i in range(N, 0, -1):
    flag = i
    value = 0
    for j in range(N, i, -1):
        if numbers[i] > numbers[j] and dp[1][j] > value:
            flag = j
            value = dp[1][j]
    if flag == i:
        dp[1][i] = 1
    else:
        dp[1][i] = dp[1][flag] + 1

result = 0
for x, y in zip(dp[0], dp[1]):
    result = max(result, x+y)
print(result-1)
