from collections import deque
from itertools import combinations
import sys, copy
input = sys.stdin.readline

dx,dy = [-1,1,0,0],[0,0,-1,1]
def BFS(graph, virus, wall):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    result = 0

    for x, y in virus:
        q.append((x, y))
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    result = max(result, visited[nx][ny])
                    q.append((nx, ny))
    
    cnt = len([(i,j) for i in range(N) for j in range(N) if visited[i][j] == -1])
    if cnt == wall:
        return True, result
    else:
        return False, result

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

candidate = [(i,j) for i in range(N) for j in range(N) if arr[i][j] == 2]
# result = sys.maxsize
result = []
for row in combinations(candidate, M):
    arr_copy = copy.deepcopy(arr)
    walls = len([(i,j) for i in range(N) for j in range(N) if arr_copy[i][j] == 1])
    cond, count = BFS(arr_copy, row, walls)
    if cond: result.append(count)

print(min(result)) if result else print(-1)