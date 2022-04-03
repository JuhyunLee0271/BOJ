from collections import deque
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

temp = []
result = []
q =  deque()
q.append((0, 0, C))
while q:
    a, b, c = q.popleft()
    if 0 <= a <= A and 0 <= b <= B and 0 <= c <= C:
        if (a, b, c) not in temp:
            temp.append((a, b, c))
            if a == 0:
                result.append(c)
        else: continue
        
        for command in ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']:
            if command == 'ab':
                water = min(a, B - b)
                q.append((a-water, b+water, c))
            elif command == 'ac':
                water = min(a, C - c)
                q.append((a-water, b, c+water))
            elif command == 'ba':
                water = min(b, A - a)
                q.append((a+water, b-water, c))
            elif command == 'bc':
                water = min(b, C - c)
                q.append((a, b-water, c+water))
            elif command == 'ca':
                water = min(c, A - a)
                q.append((a+water, b, c-water))
            elif command == 'cb':
                water = min(c, B - b)
                q.append((a, b+water, c-water))

print(*sorted(result))