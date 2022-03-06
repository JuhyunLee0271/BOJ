N = int(input())
dp = [0] * (N+1)
arr = [0] + list(map(int, input().split()))
dp[0] = 0
dp[1] = arr[1]

for i in range(2, N+1):
    temp = [] 
    for j in range(i):
        temp.append(dp[j] + arr[i-j])
    dp[i] = max(temp)

print(dp[N])
