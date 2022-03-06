T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    dp = [[0] * (N) for i in range(2)]
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    if N == 1:
        print(max(map(max, arr)))
        continue

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = max(dp[1][0] + arr[0][1], dp[0][0])
    dp[1][1] = max(dp[0][0] + arr[1][1], dp[1][0])

    for j in range(2, N):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i][j-2], dp[i+1][j-2], dp[i+1][j-1]) + arr[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-2], dp[i][j-2], dp[i-1][j-1]) + arr[i][j]

    print(max(map(max, dp)))

            
    
    