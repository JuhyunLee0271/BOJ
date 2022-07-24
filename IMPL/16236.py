from collections import deque

def get_distance(shark, ex, ey):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    q = deque()
    q.append([shark[0], shark[1], 0])
    visited = set()
    visited.add((shark[0], shark[1]))
    
    while q:
        x, y, dist = q.popleft()
        if x == ex and y == ey:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 상어의 크기보다 같거나 작은 칸은 지나갈 수 있음 
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and board[nx][ny] <= shark[2]:
                q.append([nx, ny, dist + 1])
                visited.add((nx, ny))
                    
# 먹을 수 있는 물고기 중 거리가 가장 가까운, 위쪽-왼쪽 기준 정렬
def find_food(shark, fishes):
    result = []
    for x, y, size in fishes:
        if size < shark[2] and (x, y) not in dead_fishes: # 상어보다 사이즈가 작다면 -> 먹을 수 있음
            distance = get_distance(shark, x, y)
            if distance:
                result.append([x, y, distance])
    if not result:
        return []
    else:
        # 거리, 위쪽, 아래쪽 정렬 
        result.sort(key=lambda x:(x[2], x[0], x[1]))
        return result[0]

# find_food를 통해 얻은 좌표값으로 이동, 자신과 같은 크기의 물고기를 먹는다면 크기를 1 증가 
dx, dy = [-1,1,0,0], [0,0,-1,1]
def move_to_eat(shark, fishes, target_fish):
    global answer, eat_cnt
    fx, fy, f_dist = target_fish[0], target_fish[1], target_fish[2]
    eat_cnt += 1
    
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    if shark[2] == eat_cnt:
        shark = [fx, fy, shark[2] + 1]
        eat_cnt = 0
    else:
        shark = [fx, fy, shark[2]]
    
    dead_fishes.add((fx, fy))
    answer += f_dist
    
    return shark, fishes
                
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

fishes = []
dead_fishes = set()
shark = []
answer = 0
eat_cnt = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = [i, j, 2]       
            board[i][j] = 0
        elif board[i][j] in [1, 2, 3, 4, 5, 6]:
            fishes.append([i, j, board[i][j]])

while True:
    target_fish = find_food(shark, fishes)
    if not target_fish:
        break
    shark, fishes = move_to_eat(shark, fishes, target_fish)

print(answer)