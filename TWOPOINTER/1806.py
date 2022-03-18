import sys
input = sys.stdin.readline
INF = sys.maxsize

N,S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
total = 0
result = INF

while True:
    if total >= S:
        result = min(result, end-start)
        total -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        total += arr[end]
        end += 1

print(0) if result == INF else print(result)