import sys
input = sys.stdin.readline

def check(x):
    indegree = 0
    outdegree = 0

    for i in range(1, N+1):
        if graph[x][i] == 1:
            outdegree += 1
        elif graph[i][x] == 1:
            indegree += 1
    
    if (outdegree > N // 2) or (indegree > N // 2):
        return True
    else:
        return False

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

result = []
for i in range(1, N+1):
    result.append(check(i))
print(result.count(True))
