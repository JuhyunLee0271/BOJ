from collections import deque

def BFS(x, y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx,ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    arr = []
    for i in range(N):
        arr.append([0]*M)

    for i in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                BFS(i,j)
                cnt += 1
    print(cnt)