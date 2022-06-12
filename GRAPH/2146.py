from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y, cnt):
    q = deque()
    q.append([x, y])
    visited[x][y] = cnt
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and arr[nx][ny] == 1:
                visited[nx][ny] = cnt
                q.append([nx, ny])

    return [[i, j] for i in range(N) for j in range(N) if visited[i][j] == cnt]

def solution(island):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    
    for x, y in island:
        q.append([x, y, 0])
        visited[x][y] = True
    
    num_island = island_dict[(x, y)] 
    
    while q:
        x, y, cnt = q.popleft()
        if arr[x][y] == 1 and island_dict[(x, y)] != num_island:
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 1 and island_dict[(nx, ny)] == num_island:
                    q.append([nx, ny, cnt])
                    visited[nx][ny] = True
                else:
                    q.append([nx, ny, cnt + 1])
                    visited[nx][ny] = True

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

island = []
island_dict = {}
visited = [[-1] * N for _ in range(N)]
cnt = 1

for i in range(N):
    for j in range(N):
        if visited[i][j] == -1 and arr[i][j] == 1:
            island.append(BFS(i, j, cnt))
            cnt += 1

for i in range(len(island)):
    for a, b in island[i]:
        island_dict[(a, b)] = i+1

answer = sys.maxsize
for land in island:
    answer = min(answer, solution(land) - 1)

print(answer)

    

        