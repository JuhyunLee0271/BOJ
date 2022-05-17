from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
visited = [[False] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
q = deque()
q.append([r1, c1, 0])
visited[r1][c1] = True
dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

while q:
    x, y, cnt = q.popleft()
    if x == r2 and y == c2:
        break
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append([nx, ny, cnt + 1])

print(-1) if not visited[r2][c2] else print(cnt)