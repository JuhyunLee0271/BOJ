import sys
input = sys.stdin.readline
N = int(input())

temp = list(map(int, input().split()))

min_dp = temp
max_dp = temp

for _ in range(N-1):
    a, b, c = map(int, input().split())
    min_dp = [a + min(min_dp[:2]), b + min(min_dp), c + min(min_dp[1:])]
    max_dp = [a + max(max_dp[:2]), b + max(max_dp), c + max(max_dp[1:])]

print(max(max_dp), min(min_dp))