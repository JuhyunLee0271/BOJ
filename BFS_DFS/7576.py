from collections import deque

def BFS():
    q = deque()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
    
    return max(map(max, arr)) - 1

M,N = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

result = BFS()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result = -1

print(result)
