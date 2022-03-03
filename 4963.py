from collections import deque

# 1은 땅, 0은 바다일 때
# bfs로 1일 때 접해있는 모든 1(땅)을 0(바다로) 만든 뒤 count를 증가
def BFS(vertex):
    q = deque()
    q.append(vertex)
    arr[vertex[0]][vertex[1]] = '0'

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,1,-1,1,-1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '1':
                arr[nx][ny] = '0'
                q.append((nx,ny))

while True:                    
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    for i in range(h):
        arr.append([])
    for i in range(h):
        arr[i] = list(input().split())

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '1':
                BFS((i,j))
                cnt += 1

    print(cnt)

