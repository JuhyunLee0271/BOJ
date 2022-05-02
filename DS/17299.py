from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
counter = dict(Counter(arr).items())
stack = []
result = [-1] * N

for i in range(N):
    while stack and counter[stack[-1][1]] < counter[arr[i]]:
        idx, val = stack.pop()
        result[idx] = arr[i]
    stack.append([i, arr[i]])

print(*result)
        