from collections import deque
import copy

def BFS(x, y, arr):
    q = deque()
    q.append((x,y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    target = arr[x][y] 
    arr[x][y] = '0'
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == target:
                arr[nx][ny] = '0'
                q.append((nx,ny))

N = int(input())
arr = []
arr_2 = []
cnt_1 = 0
cnt_2 = 0

for _ in range(N):
    arr.append(list(input()))

arr_2 = copy.deepcopy(arr)

for i in range(N):
    for j in range(N):
        if arr_2[i][j] == 'G':
            arr_2[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if arr[i][j] != '0':
            BFS(i,j,arr)
            cnt_1 += 1
        
        if arr_2[i][j] != '0':
            BFS(i,j,arr_2)
            cnt_2 += 1
            
print(cnt_1, cnt_2)
