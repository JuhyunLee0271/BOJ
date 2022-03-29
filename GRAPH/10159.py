import sys
input = sys.stdin.readline

def check(x):
    count = 0
    for i in range(1, N+1):
        if graph[i][x] == 1: count += 1
        elif graph[x][i] == 1: count += 1
    
    return N-1-count

N = int(input())
M = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b][a] = 1 

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for i in range(1, N+1):
    print(check(i))
