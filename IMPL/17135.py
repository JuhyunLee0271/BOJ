import sys, copy
input = sys.stdin.readline

def backtracking(cur_list: list = [], cur: int = 0):
    global archers
    if len(cur_list) == 3:
        result = []
        for pos in cur_list:
            result.append([N, pos])
        archers.append(result.copy())
        return
    
    for i in range(cur, M):
        cur_list.append(i)
        backtracking(cur_list, i + 1)
        cur_list.pop()
    return

def move(enemies: list):
    new_enemies = []
    for x, y in enemies:
        # 적이 성에 도달했을 경우 제외
        if x != N-1:
            new_enemies.append([x+1, y])
    return new_enemies
    
def attack(archers: list, enemies: list):
    # 궁수 한 명씩 제거할 적 선택. 거리 - 왼쪽 순
    attack_set = set()
    kill_cnt = 0
    for archer in archers:
        enemy_dist = []
        for enemy in enemies:
            dist = abs(archer[0] - enemy[0]) + abs(archer[1] - enemy[1])
            if dist <= D:
                enemy_dist.append([enemy[0], enemy[1], dist])
        if enemy_dist:
            enemy_dist.sort(key=lambda x:(x[2], x[1]))
            attack_set.add((enemy_dist[0][0], enemy_dist[0][1]))
    
    # 가장 가까운 적 제거
    for x, y in list(attack_set):
        if [x, y] in enemies:
            enemies.remove([x, y])
            kill_cnt += 1
    
    # 죽인 적의 수를 리턴
    return kill_cnt

def solution(archer: list, enemies: list):
    result = 0 
    while True:
        result += attack(archer, enemies)
        enemies = move(enemies)
        if not enemies:
            return result

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
enemies = [[x, y] for x in range(N) for y in range(M) if board[x][y] == 1]
archers = []
answer = 0
backtracking()

for archer in archers:
    _enemies = copy.deepcopy(enemies)
    answer = max(answer, solution(archer, _enemies))

print(answer)