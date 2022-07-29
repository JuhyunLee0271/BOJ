import sys
input = sys.stdin.readline

# 북, 동, 남, 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
convert_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
def get_direction(direction, command):
    if command == 'L':
        return (direction - 1) % 4
    elif command == 'R':
        return (direction + 1) % 4

# 벽이나 로봇에 박는지 판단 
def check(n, x, y):
    if 0 <= x < B and 0 <= y < A:
        for key, value in robots.items():
            if key == n:
                continue
            if value[0] == x and value[1] == y:
                print(f"Robot {n} crashes into robot {key}")
                sys.exit(0)
    else:
        print(f"Robot {n} crashes into the wall")
        sys.exit(0)
    return

# A, B 크기의 땅 
A, B = map(int, input().split())

# N개의 로봇, M개의 명령
N, M = map(int, input().split())
robots = dict()
commands = []
# L: 방향을 왼쪽으로 90도, R: 방향을 오른쪽으로 90도, F: 앞으로 한 칸 움직임
for idx in range(N):
    a, b, direction = input().rstrip().split()
    x = B-int(b)
    y = int(a)-1
    robots[idx+1] = [int(x), int(y), convert_dict[direction]]
    
for _ in range(M):
    a, b, c = input().rstrip().split()
    commands.append([int(a), b, int(c)])

for robot, command, cnt in commands:        
    for _ in range(cnt):
        x, y, _dir = robots[robot]
        # 방향만 바꿈
        if command in ['L', 'R']:
            _dir = get_direction(_dir, command)
            robots[robot] = [x, y, _dir]
        # 앞으로 전진
        elif command == 'F':
            nx, ny = x + dx[_dir], y + dy[_dir]
            check(robot, nx, ny)
            robots[robot] = [nx, ny, _dir]
            
print("OK")

