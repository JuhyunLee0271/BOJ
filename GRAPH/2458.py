import sys
input = sys.stdin.readline

def check(x):
    count = 0
    # degree check
    for i in range(1, N+1):
        if graph[i][x] == 1:
            count += 1
        elif graph[x][i] == 1:
            count += 1

    if count == N-1:
        return True
    else:
        return False    

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
result = []
for i in range(1, N+1):
    result.append(check(i))

print(result.count(True))
