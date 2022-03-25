import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
arr = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = INF
for i in range(1, V+1):
    result = min(result, arr[i][i])

print("-1") if result == INF else print(result)