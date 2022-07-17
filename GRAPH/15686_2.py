from collections import deque
import sys, copy
input = sys.stdin.readline

def backtracking(cur_list:list = list(), cur: int = 0):
    global combi
    if len(cur_list) == (len(chickens) - M):
        combi.append(copy.deepcopy(cur_list))
        return
    
    for idx in range(cur, len(chickens)):
        cur_list.append(chickens[idx])
        backtracking(cur_list, idx + 1)
        cur_list.pop()
    return

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(arr, comb):
    for x, y in comb:
        arr[x][y] = 0
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    result = []
    
    for x, y in chickens:
        if [x, y] not in comb:
            q.append([x, y])
            dist[x][y] = 0
    
    while q:
        x, y = q.popleft()
        if len(result) == len(houses):
            return sum(result)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1 and (arr[nx][ny] == 0 or arr[nx][ny] == 1):
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
                if arr[nx][ny] == 1:
                    result.append(dist[nx][ny])    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
combi = []
answer = 10e9

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append([i, j])
        elif board[i][j] == 2:
            chickens.append([i, j])

backtracking()

for comb in combi:
    temp_board = copy.deepcopy(board)
    answer = min(answer, BFS(temp_board, comb))

print(answer)