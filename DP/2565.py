import sys
input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
    a,b = map(int, input().split())
    lines.append((a, b))

numbers = []
dp = [0] * N
for e in sorted(lines):
    numbers.append(e[1])

dp[0] = 1
for i in range(1, N):
    flag = i
    val = 0
    for j in range(i):
        if numbers[i] > numbers[j] and dp[j] > val:
            flag = j
            val = dp[j]
    if flag == i:
        dp[i] = 1
    else:
        dp[i] = dp[flag] + 1

print(N-max(dp))
