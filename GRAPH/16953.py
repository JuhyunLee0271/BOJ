from collections import deque
import sys
input = sys.stdin.readline

start, end = map(int, input().split())

q = deque()
q.append((start, 1))

result = -1
while q:
    x, cnt = q.popleft()
    if x == end:
        result = cnt
    for i in range(2):
        if i == 0:
            nx = 2*x
        else:
            nx = int(str(x) + '1')
        if start <= nx <= end:
            q.append((nx, cnt+1))

print(result)