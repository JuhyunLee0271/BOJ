import sys
input = sys.stdin.readline

def get_fish(col):
    global answer
    for row in range(R):    
        for key, value in sharks.items():
            r, c, s, d, z = value
            # 해당하는 열의 가장 땅에서 가까운 물고기를 잡음
            if row == r and col == c:
                del sharks[key]
                answer += z
                return

def get_position(r, c, s, d, z):
    nr, nc, nd = r, c, d
    for _ in range(s):
        nr, nc = r + dx[d], c + dy[d]
        if 0 <= nr < R and 0 <= nc < C:
            r, c = nr, nc
            continue
        else:
            if d == 1: nd = 2
            if d == 2: nd = 1
            if d == 3: nd = 4
            if d == 4: nd = 3
            nr, nc = r + dx[nd], c + dy[nd]
            r, c, d = nr, nc, nd
    
    return nr, nc, s, nd, z
            
def move_shark():
    # 상어들이 각자 속도, 방향에 따라 움직임
    for key, value in sharks.items():
        r, c, s, d, z = get_position(*value)
        sharks[key] = [r, c, s, d, z]
    
    pos_count = dict()
    del_shark = []
    for key, value in sharks.items():
        r, c, s, d, z = value
        if (r, c) in pos_count: pos_count[(r, c)] += 1
        else: pos_count[(r, c)] = 1

    # 2마리 이상의 상어가 한 칸에 존재하는 경우 
    for x, y in [key for key, value in pos_count.items() if value > 1]:
        flag, size = -1, -1
        _temp = []
        for key, value in sharks.items():
            r, c, s, d, z = value
            if x == r and y == c:
                _temp.append([key, z])
                if z > size:
                    flag = key
                    size = z
        eat_amount = 0
        for key, size in _temp:
            if key != flag:
                eat_amount += size
                del_shark.append(key)
    
    for key in del_shark:
        del sharks[key]
                
# 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]
sharks = dict()
answer = 0

R, C, M = map(int, input().split())
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[i+1] = [r-1, c-1, s, d, z]

for col in range(C):
    get_fish(col)
    move_shark()

print(answer)

