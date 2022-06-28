import sys
input = sys.stdin.readline

# 현재 위치와 방향에서 왼쪽이 청소가능한 지 판단
def is_blank(x, y, dir):
    if dir == 0:
        if arr[x][y-1] == 0 and not visited[x][y-1]: return True
    elif dir == 1:
        if arr[x-1][y] == 0 and not visited[x-1][y]: return True
    elif dir == 2:
        if arr[x][y+1] == 0 and not visited[x][y+1]: return True
    elif dir == 3:
        if arr[x+1][y] == 0 and not visited[x+1][y]: return True
    return False

# 현재 위치에서 뒤쪽이 벽인지 판단
def is_wall(x, y, dir):
    if dir == 0:
        if arr[x+1][y] == 1: return True
    elif dir == 1:
        if arr[x][y-1] == 1: return True
    elif dir == 2:
        if arr[x-1][y] == 1: return True
    elif dir == 3:
        if arr[x][y+1] == 1: return True
    return False

# 왼쪽으로 방향을 회전
def change_direction(dir):
    return (dir-1)%4

# 직진
def go_straight(x, y, dir):
    if dir == 0:
        return x-1, y
    elif dir == 1:
        return x, y+1
    elif dir == 2:
        return x+1, y
    elif dir == 3:
        return x, y-1

# 후진
def go_back(x, y, dir):
    if dir == 0:
        return x+1, y
    elif dir == 1:
        return x, y-1
    elif dir == 2:
        return x-1, y
    elif dir == 3:
        return x, y+1

N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[R][C] = True

answer, cnt = 1, 0

x, y, dir = R, C, D

while True:
    # 연속 4번 방향 회전을 한다면 후진. 뒤가 벽이라면 종료
    if cnt == 4:
        if is_wall(x, y, dir):
            print(answer)
            break
        else:
            nx, ny = go_back(x, y, dir)
            x, y = nx, ny
            cnt = 0
            continue
    
    # 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면 
    if is_blank(x, y, dir):
        new_dir = change_direction(dir)
        nx, ny = go_straight(x, y, new_dir)
        visited[nx][ny] = True
        
        answer += 1
        cnt = 0
        x, y, dir = nx, ny, new_dir
        continue
    
    # 그렇지 않을 경우 왼쪽으로 회전만
    else:
        dir = change_direction(dir)
        cnt += 1
        continue
