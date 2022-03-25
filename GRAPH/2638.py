from collections import deque
import sys
input = sys.stdin.readline

dx,dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    q.append((nx, ny))
    
    target = [(i,j) for i in range(N) for j in range(M) if arr[i][j] == 1]
    for x, y in target:
        q.append((x, y))
    
    cheese = []

    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 2: 
                    cnt += 1
        if cnt >= 2:
            cheese.append((x, y))

    for x, y in cheese:
        arr[x][y] = 0
    
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                arr[i][j] = 0
            if arr[i][j] == 1:
                result += 1
    return result        

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = 0
while True:
    res = BFS(0,0)
    result += 1
    if res == 0:
        break
print(result)