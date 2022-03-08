import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
dp[1] = 1
arr = [0] + list(map(int, input().split()))

for i in range(2, N+1):
    val =  0
    flag = i
    for j in range(i):
        if arr[j] < arr[i] and val < dp[j]:
            val = dp[j]
            flag = j
    if flag == i: dp[i] = 1
    else: dp[i] = dp[flag] + 1

print(max(dp))
        

