from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

q = deque()
q.append((S, 0))
cost = [-1] * 1000001
cost[S] = 0

while q:
    pos, cnt = q.popleft()
    if pos == G:
        break
    for npos in (pos + U, pos - D):
        if 1 <= npos <= F and cost[npos] == -1:
            cost[npos] = cost[pos] + 1
            q.append((npos, cnt+1))

print("use the stairs") if cost[G] == -1 else print(cost[G])