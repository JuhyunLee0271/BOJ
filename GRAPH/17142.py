from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(pair):
    q = deque()
    dist = [[-1] * N for _ in range(N)]
    for x, y in pair:
        q.append((x, y))
        dist[x][y] = 0
        
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    
    
    max_val = 0
    wall_cnt, clean_cnt = 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                max_val = max(max_val, dist[i][j])
            if graph[i][j] == 1: wall_cnt += 1
            if dist[i][j] == -1: clean_cnt += 1
    
    return max_val if wall_cnt == clean_cnt else sys.maxsize

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = [(i,j) for i in range(N) for j in range(N) if graph[i][j] == 2]
result = sys.maxsize

for pair in list(combinations(virus, M)):
    result = min(BFS(pair), result)

print(-1) if result == sys.maxsize else print(result)