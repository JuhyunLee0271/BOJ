N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N
dp[0] = arr[0]

for i in range(1, len(arr)):
    max_val = 0
    flag = i
    for j in range(i):
        if arr[j] < arr[i] and max_val < dp[j]:
            max_val = dp[j]
            flag = j
    dp[i] = dp[flag] + arr[i]
        
print(max(dp))
