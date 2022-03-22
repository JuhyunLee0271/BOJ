import sys
input = sys.stdin.readline

def DFS(x, weight):
    for next, wei in graph[x]:
        if dist[next] == -1:
            dist[next] = weight + wei
            DFS(next, weight+ wei)

N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(N):
    com = list(map(int, input().split()))
    vertex = com[0]
    target = com[1:-1]

    for i in range(0, len(target), 2):
        graph[vertex].append((target[i], target[i+1]))

dist = [-1] * (N+1)
dist[1] = 0
DFS(1, 0)
start = dist.index(max(dist))

dist = [-1] * (N+1)
dist[start] = 0
DFS(start, 0)
print(max(dist))
        