import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
dist = [0] * (N+1)

for i in range(1, N+1):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a][b] = graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_val = INF
for i in range(1, N+1):
    min_val = min(min_val, max(graph[i][1:]))

result = []
for i in range(1, N+1):
    if min_val == max(graph[i][1:]):
        result.append(i)
result.sort()

print(min_val, len(result))
print(*result)