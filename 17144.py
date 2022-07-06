import sys
input = sys.stdin.readline

def spread_dust():
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    candidate = [[i, j] for i in range(R) for j in range(C) if arr[i][j] > 0]
    spread = []
    
    for x, y in candidate:   
        dust = int(arr[x][y]/5)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                spread.append([x, y, nx, ny, dust])
        
    for x, y, nx, ny, dust in spread:
        arr[x][y] -= dust
        arr[nx][ny] += dust
    
def operate_air_cleaner(option):
    up, down = cleaners
    # up_cycle
    if option == 0: 
        dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
        x, y = up, 1
    # down_cycle
    else: 
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x, y = down, 1
    
    direction, temp = 0, 0
    
    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if (x == up or x == down) and y == 0:
            break
        if 0 <= nx < R and 0 <= ny < C:
            arr[x][y], temp = temp, arr[x][y]
            x, y = nx, ny
        else:
            direction += 1
                            
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
cleaners = sorted([i for i in range(R) for j in range(C) if arr[i][j] == -1])

while T:    
    spread_dust()
    operate_air_cleaner(0)
    operate_air_cleaner(1)
    T -= 1

print(sum([arr[i][j] for i in range(R) for j in range(C) if arr[i][j] > 0]))