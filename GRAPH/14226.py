from collections import deque
import sys
input = sys.stdin.readline

S = int(input())

q = deque()
q.append((1, 0))
visited = dict()
visited[(1,0)] = 0

while q:
    s, c = q.popleft()
    if s == S:
        print(visited[(s, c)])
        break
    
    if (s, s) not in visited.keys():
        visited[(s, s)] = visited[(s, c)] + 1
        q.append((s, s))
    if (s-1,c) not in visited.keys():
        visited[(s-1,c)] = visited[(s, c)] + 1
        q.append((s-1, c))
    if (s+c,c) not in visited.keys():
        visited[(s+c, c)] = visited[(s, c)] + 1
        q.append((s+c, c))

