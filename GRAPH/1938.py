from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def move(a, b, c, dir):
    if dir in [0, 1, 2, 3]:
        x1, y1 = a[0] + dx[dir], a[1] + dy[dir]
        x2, y2 = b[0] + dx[dir], b[1] + dy[dir]
        x3, y3 = c[0] + dx[dir], c[1] + dy[dir]
        if 0 <= x1 < N and 0 <= y1 < N and 0 <= x2 < N and 0 <= y2 < N and 0 <= x3 < N and 0 <= y3 < N:
            if board[x1][y1] != '1' and board[x2][y2] != '1' and board[x3][y3] != '1':
                return [[x1, y1], [x2, y2], [x3, y3]]
    # 회전일 때
    elif dir == 4:
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c
        # 가로일 때 회전
        if x1 == x2 == x3:
            x4, x5, x6, y4, y5, y6 = x1-1, x1-1, x1-1, y1, y2, y3
            x7, x8, x9, y7, y8, y9 = x1+1, x1+1, x1+1, y1, y2, y3
            if 0 <= x4 < N and 0 <= x5 < N and 0 <= x6 < N and 0 <= x7 < N and 0 <= x8 < N and 0 <= x9 < N:
                if 0 <= y4 < N and 0 <= y5 < N and 0 <= y6 < N and 0 <= y7 < N and 0 <= y8 < N and 0 <= y9 < N:
                    if board[x4][y4] != '1' and board[x5][y5] != '1' and board[x6][y6] != '1' and board[x7][y7] != '1' and board[x8][y8] != '1' and board[x9][y9] != '1':
                        return [[x2-1, y2], [x2, y2], [x2+1, y2]]
        # 세로일 때 회전
        else:
            x4, x5, x6, y4, y5, y6 = x1, x2, x3, y1-1, y1-1, y1-1
            x7, x8, x9, y7, y8, y9 = x1, x2, x3, y1+1, y1+1, y1+1
            if 0 <= x4 < N and 0 <= x5 < N and 0 <= x6 < N and 0 <= x7 < N and 0 <= x8 < N and 0 <= x9 < N:
                if 0 <= y4 < N and 0 <= y5 < N and 0 <= y6 < N and 0 <= y7 < N and 0 <= y8 < N and 0 <= y9 < N:
                    if board[x4][y4] != '1' and board[x5][y5] != '1' and board[x6][y6] != '1' and board[x7][y7] != '1' and board[x8][y8] != '1' and board[x9][y9] != '1':
                        return [[x2, y2-1], [x2, y2], [x2, y2+1]]
            
    return False

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
start, end = [], []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            start.append([i, j])
            board[i][j] = '0'
        elif board[i][j] == 'E':
            end.append([i, j])
            board[i][j] = '0'

q = deque()
q.append(start + [0])
visited = set()
visited.add(((start[0][0], start[0][1]), (start[1][0], start[1][1]), (start[2][0], start[2][1])))

while q:
    a, b, c, cnt = q.popleft()
    if a == end[0] and b == end[1] and c == end[2]:
        print(cnt)
        sys.exit(0)
    for i in range(5):
        result = move(a, b, c, i)
        if result:
            na, nb, nc = result
            if ((na[0], na[1]), (nb[0], nb[1]), (nc[0], nc[1])) not in visited:
                visited.add(((na[0], na[1]), (nb[0], nb[1]), (nc[0], nc[1])))
                q.append([na, nb, nc, cnt + 1])
print(0)