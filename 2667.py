from collections import deque

def BFS(x, y, target):
    q = deque()
    q.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    arr[x][y] = target

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:    
                arr[nx][ny] = target
                q.append((nx,ny))

n = int(input())

arr = []
target = 2
numbers = dict()

for i in range(n):
    arr.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            BFS(i, j, target)
            target += 1

for i in range(n):
    for j in range(n):
        if not arr[i][j] == 0:
            if numbers.get(arr[i][j]):
                numbers[arr[i][j]] += 1
            else:
                numbers[arr[i][j]] = 1

print(len(numbers))
for e in sorted(numbers.values()):
    print(e)

