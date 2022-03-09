import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
result = 1
for _ in range(N):
    arr.append(list(map(int, input().rstrip('\n'))))
    
for i in range(N-1):
    for j in range(M-1):
        for k in range(min(N,M)):
            if ((i + k) < N and (j + k) < M) and (arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]):
                result = max(result, (k+1)**2)

print(result)

