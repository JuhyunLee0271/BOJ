from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def move(x, y, dx, dy):
    count = 0
    while True:
        if board[x][y] == 'O':
            break
        if board[x+dx][y+dy] == '#':
            break
        x += dx
        y += dy
        count += 1
    return x, y, count

def BFS(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited = set()
    visited.add((rx, ry, bx, by))
    
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            break               
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(cnt)
                    return
                # 겹쳐 있을 경우
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if ((nrx, nry, nbx, nby)) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby, cnt + 1))
    print(-1)

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

BFS(rx, ry, bx, by)