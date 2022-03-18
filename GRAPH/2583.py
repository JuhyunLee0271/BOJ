from collections import deque

def BFS(arr, x, y, target):
    q = deque()
    q.append((x, y))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    arr[x][y] = target + 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = target + 1
                q.append((nx, ny))

M,N,K = map(int, input().split())
arr = []
for _ in range(M):
    arr.append([0]*N)

for _ in range(K):
    a,b,c,d = map(int, input().split())
    
    a = a
    b = (M-b-1)
    c -= 1
    d = (M-d)

    for i in range(d, b+1):
        for j in range(a, c+1):
            arr[i][j] = -1

target = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            BFS(arr, i, j, target)
            target += 1

numbers = dict()

for i in range(M):
    for j in range(N):
        if arr[i][j] != -1:
            if arr[i][j] not in numbers:
                numbers[arr[i][j]] = 1
            else:
                numbers[arr[i][j]] += 1

print(len(numbers))
print(*sorted(numbers.values()))