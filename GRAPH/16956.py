from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if arr[nx][ny] == 'S':
                    print(0)
                    sys.exit()

    print(1)
    return

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
q = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == '.':
            arr[i][j] = 'D'
        if arr[i][j] == 'W':
            q.append([i, j])
            visited[i][j] = True

BFS()
for i in range(R):
    for j in range(C):
        print(arr[i][j], end='')
    print()
