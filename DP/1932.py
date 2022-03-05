N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = []
for i in range(N):
    dp.append([0]*(i+1))

dp[0][0] = arr[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(arr[i][j] + dp[i-1][j], arr[i][j] + dp[i-1][j-1])

print(max(dp[N-1]))

