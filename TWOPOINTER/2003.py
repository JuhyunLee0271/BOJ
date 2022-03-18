import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
total = 0
result = 0

while start <= end and end <= N:
    total = sum(arr[start:end])
    
    if total == M:
        result += 1
        start += 1
        end += 1
    elif total < M:
        end += 1
    elif total > M:
        start += 1
    
print(result)

