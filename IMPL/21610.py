import sys
input = sys.stdin.readline

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move(dir, cnt):
    global clouds, new_clouds
    visited = set()
    
    for i in range(len(clouds)):
        x, y = clouds[i]
        nx = (x + dx[dir]*cnt)%N
        ny = (y + dy[dir]*cnt)%N
        clouds[i] = [nx, ny]
    
    for x, y in clouds:
        board[x][y] += 1
        visited.add((x, y))
        
    for x, y in clouds:
        cnt = check_diagonal(x, y)
        board[x][y] += cnt
    
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in visited:
                board[i][j] -= 2
                new_clouds.append([i, j])
    
    clouds = new_clouds
    
def check_diagonal(x, y):
    result = 0
    for nx, ny in [[x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1]]:
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
            result += 1
    return result

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
new_clouds = []

for _ in range(M):
    dir, cnt = map(int, input().split())
    move(dir, cnt)

print(sum([sum(x) for x in board]))