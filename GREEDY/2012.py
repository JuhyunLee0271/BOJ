import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

result = 0
for i in range(N):
    result += abs(i+1-arr[i])
print(result)
    