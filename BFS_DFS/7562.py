from collections import deque

def BFS(arr, x, y, e1, e2):
    q = deque()
    q.append((x, y))

    dx = [-2,-1,1,2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    while q:
        x,y = q.popleft()
        if x == e1 and y == e2:
            print(arr[x][y])
            return True
        for i in range(8):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append([0]*N)

    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())

    BFS(arr, s1, s2, e1, e2)

