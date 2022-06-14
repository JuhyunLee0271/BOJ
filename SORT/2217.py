import sys
input = sys.stdin.readline
answer = 0

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

for k in range(1, N+1):
    answer = max(answer, k*arr[-k])

print(answer)

    