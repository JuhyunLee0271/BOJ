import sys, copy
input = sys.stdin.readline

# make permutations of operations
def make_permu(cur_list:list = list(), visited:set = set()):
    global permutations, K
    if len(cur_list) == K:
        permutations.append(copy.deepcopy(cur_list))
        return
        
    for idx in range(len(command)):
        target = tuple(command[idx])
        if (target) not in visited:
            cur_list.append(command[idx])
            visited.add((target))
            make_permu(cur_list, visited)
            cur_list.pop()
            visited.remove((target))
    return

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
def rotate_array(r, c, s, arr):
    sx, sy = r-s-1, c-s-1
    ex, ey = r+s-1, c+s-1
    
    start_list = []
    end_list = []
    for i in range(s):
        start_list.append([sx+i, sy+i])    
        end_list.append([ex-i, ey-i])
            
    for num in zip(start_list, end_list):
        sx, sy = num[0] # 가장 왼쪽 위 (시작점)
        ex, ey = num[1] # 가장 오른쪽 아래 
        before = arr[sx+1][sy]  # 가장 왼쪽 위의 하나 아래칸의 값을 before에 넣음 -> 첫 시작점에 넣을것 
        _dir = 0
        x, y = sx, sy
        
        while True:
            if x == sx and y == sy and _dir == 3:
                break
            
            current = arr[x][y]
            arr[x][y] = before
            current, before = before, current
            
            nx, ny = x + dx[_dir], y + dy[_dir]
            
            if sx <= nx <= ex and sy <= ny <= ey:
                x, y = nx, ny
                continue
            else:
                _dir += 1
                nx, ny  = x + dx[_dir], y + dy[_dir]
                x, y = nx, ny
    return arr

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(K)]
permutations = []
answer = 10e9
make_permu()

for command in permutations:
    arr = copy.deepcopy(board)
    for com in command:
        arr = rotate_array(*com, arr)    
    result = min([sum(row) for row in arr])
    answer = min(answer, result)

print(answer)
