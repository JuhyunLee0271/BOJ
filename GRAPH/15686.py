from collections import deque
from itertools import combinations
import sys, copy
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(arr):
    start = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
    end = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 1]
    target = len(end)
    
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for x, y in start:
        q.append((x, y))
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        if target == 0:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and arr[nx][ny] != 2:
                if arr[nx][ny] == 1: target -= 1
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    result = 0
    for x, y in end:
        result += visited[x][y]            
    return result

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chickens = [(i,j) for i in range(N) for j in range(N) if graph[i][j] == 2]
pairs = combinations(chickens, len(chickens) - M)

result = sys.maxsize

for p in pairs:
    graph_copy = copy.deepcopy(graph)
    dp = [-1]
    for x, y in p:
        graph_copy[x][y] = 0
    result = min(result, BFS(graph_copy))
print(result)