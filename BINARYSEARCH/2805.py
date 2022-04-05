import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for e in arr:
        if e >= mid:
            result += (e - mid)
    if result >= M:
        start = mid + 1
    elif result < M:
        end = mid - 1

print(end)