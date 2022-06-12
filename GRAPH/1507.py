import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[1]*N for _ in range(N)]
answer = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or i == k:
                continue
            if arr[i][j] == arr[i][k] + arr[k][j]:
                result[i][j] = 0
            elif arr[i][j] > arr[i][k] + arr[k][j]:
                answer = -1

if answer != -1:
    for i in range(N):
        for j in range(i, N):
            if result[i][j]:
                answer += arr[i][j]

print(answer)
                
            
            
                