import sys
input = sys.stdin.readline

def solution(rows, columns, queries):
    arr = [[[] for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = (j+1) + i*columns
    
    answer = []
    for query in queries:
        answer.append(rotate(arr, query))
    return answer

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def rotate(arr, query):
    x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    before, direction = arr[x1+1][y1], 0
    x, y = x1, y1
    min_val = before
    while True:
        if direction == 4:
            break
        nx, ny = x + dx[direction], y + dy[direction]
        if x1 <= nx <= x2 and y1 <= ny <= y2:
            arr[x][y], before = before, arr[x][y]
            min_val = min(min_val, before)
            x, y = nx, ny
        else:
            direction += 1
            continue
    return min_val