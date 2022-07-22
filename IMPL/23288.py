from collections import deque
import sys
input = sys.stdin.readline

def roll_dice(dice: list, dir: int):
    if dir == 0:
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif dir == 1:
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif dir == 2:
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif dir == 3:
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    
# BFS 
def get_score(x, y):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    target = board[x][y]
    q = deque()
    visited = set()
    q.append([x, y])
    visited.add((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and board[nx][ny] == target:
                visited.add((nx, ny))
                q.append([nx, ny])
    
    return len(visited)*target

def get_direction(dice:list, x:int, y:int, dir:int):
    A, B = dice[-1], board[x][y]
    
    if A == B:
        return dir
    elif A > B:
        return (dir+1)%4
    elif A < B:
        return (dir-1)%4

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# [위, 뒤, 오, 왼, 앞, 아래]
dice = [1, 2, 3, 4, 5, 6] 

dir = 1
x, y = 0, 0
answer = 0

# 0: 북, 1: 동, 2: 남, 3: 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
for _ in range(K):
    # 이동 방향으로 한 칸 굴러감 
    nx, ny = x + dx[dir], y + dy[dir]
    # 이동 방향에 칸이 있다면
    if 0 <= nx < N and 0 <= ny < M:
        dice = roll_dice(dice, dir)
        answer += get_score(nx, ny)
    # 이동 방향에 칸이 없다면 이동 방향을 반대로 굴러감
    else:
        dir = (dir+2)%4
        dice = roll_dice(dice, dir)
        nx, ny = x + dx[dir], y + dy[dir]
        answer += get_score(nx, ny)
    
    dir = get_direction(dice, nx, ny, dir)
    x, y = nx, ny

print(answer)