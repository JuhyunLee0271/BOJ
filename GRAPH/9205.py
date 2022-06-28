from collections import deque
import sys
input = sys.stdin.readline

def BFS(home):
    q = deque([home])
    visited = set()
    
    while q:
        x, y = q.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            return True
        
        for i in range(N):
            if i not in visited:
                nx, ny = conv[i][0], conv[i][1]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    q.append([nx, ny])
                    visited.add(i)
    
    return False

for _ in range(int(input())):
    N = int(input())

    home = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(N)]
    festival = list(map(int, input().split()))

    if BFS(home):
        print('happy')
    else:
        print('sad')