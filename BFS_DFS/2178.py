from collections import deque

def BFS(arr, x, y):
    q = deque()
    q.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

BFS(arr, 0, 0)
print(arr[N-1][M-1])