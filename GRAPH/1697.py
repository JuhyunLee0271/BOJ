from collections import deque
import sys
input = sys.stdin.readline

def BFS(start, end):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == end:
            return dist[end]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < 100001 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)

N, K = map(int, input().split())
dist = [0] * 100001
print(BFS(N,K))
