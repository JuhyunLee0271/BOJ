import sys
input = sys.stdin.readline

def check(x, y, k):
    for idx in range(N):
        if arr[x][idx] == k or arr[idx][y] == k:
            return False
    
    x_pos, y_pos = x // 3, y // 3
    squares = [[a, b] for a in range(3*x_pos, 3*(x_pos+1)) for b in range(3*y_pos, 3*(y_pos+1))]
    for a, b in squares:
        if arr[a][b] == k:
            return False
    return True

def backtracking(depth = 0):
    if depth == len(blanks):
        for i in range(N):
            for j in range(N):
                print(arr[i][j], end = ' ')
            print()
        sys.exit()
    
    x, y = blanks[depth]
    for num in range(1, 10):
        if check(x, y, num):
            arr[x][y] = num
            backtracking(depth + 1)
            arr[x][y] = 0
    return

N = 9
arr = [list(map(int, input().split())) for _ in range(N)]
blanks = [[x, y] for x in range(N) for y in range(N) if arr[x][y] == 0]
backtracking()