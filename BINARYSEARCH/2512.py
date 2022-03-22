import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
budget = int(input())

start, end = 0, max(arr)

while start <= end:
    mid = (start+end)//2
    num = 0
    for e in arr:
        num += min(mid, e)
    if num > budget:
        end = mid - 1
    elif num <= budget:
        start = mid + 1

print(end)


