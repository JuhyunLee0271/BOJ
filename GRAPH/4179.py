from collections import deque
import sys
input = sys.stdin.readline

"""
#: 벽
.: 지나갈 수 있는 공간
J: 초기 위치
F: 불이 난 공간
"""

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS():
    j_queue = deque(); j_dist = [[0] * C for _ in range(R)]
    f_queue = deque(); f_dist = [[0] * C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'J':
                j_queue.append([i, j])
            elif arr[i][j] == 'F':
                f_queue.append([i, j])
    
    # fire
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not f_dist[nx][ny] and arr[nx][ny] != '#':
                    f_dist[nx][ny] = f_dist[x][y] + 1        
                    f_queue.append([nx, ny])
        
    # jihoon
    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not j_dist[nx][ny] and arr[nx][ny] != '#':
                    if not f_dist[nx][ny] or j_dist[x][y] + 1 < f_dist[nx][ny]:
                        j_dist[nx][ny] = j_dist[x][y] + 1
                        j_queue.append([nx, ny])
            else:
                return j_dist[x][y] + 1
    
    return "IMPOSSIBLE"


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
print(BFS())