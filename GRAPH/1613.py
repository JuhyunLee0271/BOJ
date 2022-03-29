import sys
input = sys.stdin.readline

def check(a, b):
    if graph[a][b] == 0 and graph[b][a] == 0:
        return 0
    if graph[a][b] == 1 and graph[b][a] == 0:
        return -1
    if graph[a][b] == 0 and graph[b][a] == 1:
        return 1

N, K = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

S = int(input())
for _ in range(S):
    a, b = map(int, input().split())
    print(check(a, b))