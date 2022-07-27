from collections import deque
import sys
input = sys.stdin.readline

# 북, 동, 남, 서 
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def get_direction(dir, rotate):
    if rotate == 'L':
        return (dir-1)%4
    elif rotate == 'D':
        return (dir+1)%4

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
path = dict()
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 'A'

L = int(input())
for _ in range(L):
    cnt, direction = input().rstrip().split()
    path[int(cnt)] = direction

# 뱀은 왼쪽 끝이 꼬리, 오른쪽 끝이 머리
snake = deque()
snake.append([0, 0])
dir, elapsed = 1, 0

while True:
    x, y = snake[-1]

    if elapsed in path.keys():
        dir = get_direction(dir, path[elapsed])
        del path[elapsed]
    
    nx, ny = x + dx[dir], y + dy[dir]
    if 0 <= nx < N and 0 <= ny < N:
        if [nx, ny] in snake:
            break
        
        if board[nx][ny] == 'A':
            board[nx][ny] = 0
            snake.append([nx, ny])
    
        else:
            snake.append([nx, ny])
            snake.popleft()

    else:
        break
    elapsed += 1

print(elapsed+1)