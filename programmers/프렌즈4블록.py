def square_search(arr, x, y, m, n):
    x2, y2 = x, y+1
    x3, y3 = x+1, y
    x4, y4 = x+1, y+1
    if 0 <= x2 < m and 0 <= y2 < n and 0 <= x3 < m and 0 <= y3 < n and 0 <= x4 < m and 0 <= y4 < n:
        if arr[x][y] == arr[x2][y2] == arr[x3][y3] == arr[x4][y4]:
            return [[x, y], [x2, y2], [x3, y3], [x4, y4]]
    return []

def adjust_block(arr, m, n):
    for y in range(n):
        blocks = []
        for x in range(m):
            if arr[x][y] != '.':
                blocks.append(arr[x][y])
        blocks = ['.']*(m-len(blocks)) + blocks
        for k in range(m):
            arr[k][y] = blocks[k]

def solution(m, n, board):
    arr = [list(b) for b in board]
    answer = 0
    
    while True:
        result = set()
        for i in range(m):
            for j in range(n):
                if arr[i][j] != '.':
                    temp = square_search(arr, i, j, m, n)
                    if temp:
                        for x, y in temp:
                            result.add((x, y))
        if not result:
            break
        
        for x, y in list(result):
            arr[x][y] = '.'
        
        answer += len(result)
        adjust_block(arr, m, n)
        
    return answer