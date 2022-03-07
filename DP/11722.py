N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    long_val = 0
    flag = i
    for j in range(i):
        if arr[j] > arr[i] and long_val < dp[j]:
            long_val = dp[j]
            flag = j
    if flag == i:
        dp[i] = 1
    else:
        dp[i] = dp[flag] + 1

print(max(dp))

