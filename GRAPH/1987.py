from collections import deque
import sys
input = sys.stdin.readline

def BFS(x,y):
    global answer
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((x, y, arr[x][y]))

    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in ans:
                q.append((nx, ny, ans + arr[nx][ny]))
                answer = max(answer, len(ans)+1)

R,C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input().rstrip()))

answer = 1
BFS(0,0)
print(answer)
