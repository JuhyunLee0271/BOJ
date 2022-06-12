from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
    
dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(pair):
    x, y = pair[0]//5, pair[0]%5
    q = deque()
    q.append([x, y])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    target = []
    for pos in pair:
        target.append([pos//5, pos%5])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and [nx, ny] in target:
                q.append([nx, ny])
                visited[nx][ny] = True
    
    for a, b in target:
        if not visited[a][b]:
            return False
    
    result = ""
    for a, b in target:
        result += arr[a][b]
    return True if result.count('S') >= 4 else False    
    
# 'S' 가 최소 4명 이상 
arr = [list(input().rstrip()) for _ in range(5)]
answer = 0
for pair in combinations([i for i in range(0, 5*5)], 7):
    result = ""
    if BFS(pair):
        answer += 1
    
print(answer)
            