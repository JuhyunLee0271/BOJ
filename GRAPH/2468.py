from collections import deque
import copy

def BFS(arr, x, y):
    q = deque()
    q.append((x,y))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                arr[nx][ny] = 0
                q.append((nx,ny))

N = int(input())
result = []
numbers = []
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if arr[i][j] not in numbers:
            numbers.append(arr[i][j])

for num in numbers:
    arr_copy = copy.deepcopy(arr)
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr_copy[i][j] <= num:
                arr_copy[i][j] = 0

    for i in range(N):
        for j in range(N):
            if arr_copy[i][j] != 0:
                BFS(arr_copy, i, j)
                cnt += 1
    
    result.append(cnt)

if max(result) == 0: print(1)
else: print(max(result))


