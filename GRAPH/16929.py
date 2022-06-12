import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx, dy = [-1,1,0,0], [0,0,-1,1]
cycle = False

def DFS(x, y, curX, curY, cnt, color):
    global cycle
    if cycle: return
    visited[curX][curY] = True
    if x == curX and y == curY and cnt >= 4:
        cycle = True
        return
    
    for i in range(4):
        nx, ny = curX + dx[i], curY + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and color == arr[nx][ny]:
                DFS(x, y, nx, ny, cnt+1, color)
            elif nx == x and ny == y and cnt >= 4:
                DFS(x, y, nx, ny, cnt, color)
    return
        
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        visited[i][j] = True
        DFS(i, j, i, j, 1, arr[i][j])

print("Yes") if cycle else print("No")

            
