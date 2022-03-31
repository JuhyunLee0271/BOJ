from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))
dp = [INF] * (N+1)
dp[0] = 0

for i in range(N):
    value = arr[i]
    for j in range(1, value+1):
        if 0 <= i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

print(-1) if dp[N-1] == INF else print(dp[N-1])