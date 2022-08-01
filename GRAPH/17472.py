from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return parents[x]
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    elif a < b: parents[b] = a
    else: parents[a] = b

# 섬의 번호를 붙힘
def label_island_num(board):
    visited = set()
    island_num = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and (i, j) not in visited:
                BFS(board, i, j, island_num, visited)
                island_num += 1
    return island_num, board

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(board, x, y, island_num: int, visited: set()):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    board[x][y] = island_num
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and board[nx][ny] == 1:
                board[nx][ny] = island_num
                q.append((nx, ny))
                visited.add((nx, ny))

def make_bridge(board):
    global bridge
    # 4방향
    for d in range(4):
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    x, y = i, j
                    target = board[x][y]
                    cnt = 0
                    while True:
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if board[nx][ny] == 0:
                                cnt += 1
                            elif board[nx][ny] != 0:
                                if board[nx][ny] == target:
                                    break
                                else:
                                    if cnt >= 2:
                                        # heappush [거리, 섬1, 섬2]
                                        heappush(bridge, [cnt, target, board[nx][ny]])
                                    break
                        else:
                            break
                        x, y = nx, ny
        
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
island_num, board = label_island_num(board)
parents = [i for i in range(island_num)]
bridge = []
answer = []
make_bridge(board)

while bridge:
    cost, src, dst = heappop(bridge)
    if find(src) != find(dst):
        union(src, dst)
        answer.append(cost)

print(sum(answer)) if len(answer) == island_num - 2 else print(-1)