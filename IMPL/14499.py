import sys
input = sys.stdin.readline

def roll_dice(dices, dir):
    if dir == 1:
        return [dices[3], dices[1], dices[0], dices[5], dices[4], dices[2]]
    elif dir == 2:
        return [dices[2], dices[1], dices[5], dices[0], dices[4], dices[3]]
    elif dir == 3:
        return [dices[4], dices[0], dices[2], dices[3], dices[5], dices[1]]
    elif dir == 4:
        return [dices[1], dices[5], dices[2], dices[3], dices[0], dices[4]]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 위, 뒤, 오른쪽, 왼쪽, 앞, 아래
dices = [0]*6 

# 1: 동, 2: 서, 3: 북, 4: 남
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
for direction in command:
    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < N and 0 <= ny < M:
        dices = roll_dice(dices, direction)
        if board[nx][ny] == 0:
            board[nx][ny] = dices[-1]
        else:
            dices[-1] = board[nx][ny]
            board[nx][ny] = 0
    else:
        continue
    
    print(dices[0])
    x, y = nx, ny
    