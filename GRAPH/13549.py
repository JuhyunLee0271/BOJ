from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001
N, K = map(int, input().split())

visited = [-1] * MAX
visited[N] = 0

q = deque()
q.append(N)

while q:
    x = q.popleft()
    if x == K:
        print(visited[K])
        break
    if 0 <= x * 2 < MAX and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.appendleft(x*2)
    if 0 <= x - 1 < MAX and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if 0 <= x + 1 < MAX and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)