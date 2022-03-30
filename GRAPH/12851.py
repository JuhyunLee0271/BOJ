from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
q.append((N, 0))
visited = [-1] * 100001
visited[N] = 0

result = 0
while q:
    x, cnt = q.popleft()
    if x == K:
        result += 1
    for nx in (x-1, x+1, 2*x):
        if 0 <= nx < 100001:
            if visited[nx] == -1 or visited[nx] - visited[x] == 1:
                visited[nx] = cnt + 1
                q.append((nx, cnt+1))
print(visited[K])
print(result)

        
            