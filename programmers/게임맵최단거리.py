from collections import deque

def solution(maps):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    n, m = len(maps), len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
    return visited[n-1][m-1]