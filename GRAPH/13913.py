from collections import deque
import sys
input = sys.stdin.readline

def path(x):
    result = []
    while True:
        result.append(x)
        x = move[x]
        if x == -1:
            break
    print(len(result)-1)
    print(*result[::-1])

N, K = map(int, input().split())
move = [-1] * 100001
dist = [-1] * 100001

q = deque()
q.append(N)
dist[N] = 0

while q:
    x = q.popleft()
    if x == K:
        path(x)
        break
    for nx in (x-1, x+1, 2*x):
        if 0 <= nx < 100001:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                move[nx] = x
                q.append(nx)