import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, R = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]
cost = [0] + list(map(int, input().split()))
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if i == j: 
                graph[i][j] = 0

result = 0
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        if graph[i][j] <= M:
            temp += cost[j]
    result = max(result, temp)    
print(result)
