import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = [[INF]*(N+1) for i in range(N+1)]

M = int(input())
for _ in range(M):
    a,b,c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or arr[i][j] == INF: arr[i][j] = 0
        print(arr[i][j], end=' ')
    print()

