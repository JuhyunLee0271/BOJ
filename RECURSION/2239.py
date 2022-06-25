import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check(x, y, k):
    for idx in range(9):
        if arr[x][idx] == k:
            return False
        
    for idx in range(9):
        if arr[idx][y] == k:
            return False
    
    # 3X3 영역 
    _x, _y = x // 3, y // 3
    squares = [[a, b] for a in range(3*_x, 3*(_x+1)) for b in range(3*_y, 3*(_y+1))]
    for a, b in squares:
        if arr[a][b] == k:
            return False
        
    return True

def backtracking(depth: int):
    if depth == len(blanks):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end='')
            print()
        sys.exit()
    
    x_pos, y_pos = blanks[depth]
    for num in range(0, 10):
        if check(x_pos, y_pos, num):
            arr[x_pos][y_pos] = num
            backtracking(depth + 1)
            arr[x_pos][y_pos] = 0
    return


arr = [list(map(int, input().rstrip())) for _ in range(9)]
blanks = [[i, j] for i in range(9) for j in range(9) if arr[i][j] == 0]
backtracking(0)
