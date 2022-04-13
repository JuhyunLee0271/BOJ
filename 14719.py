import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(1, W-1):
    left, right = max(arr[:i]), max(arr[i+1:])
    result += max(0, min(left, right) - arr[i])

print(result)