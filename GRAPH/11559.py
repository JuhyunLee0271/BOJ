from collections import deque
import sys
input = sys.stdin.readline

def find_explode():
    global answer
    visited = [[False] * C for _ in range(R)]
    result = []
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] != '.' and not visited[i][j]:
                temp = BFS(i, j, visited)
                if temp: result.append(temp)
    
    if not result: return False
    
    for _result in result:
        for x,y in _result:
            arr[x][y] = '.'
    answer += 1
    return True

def adjust_block():
    for i in range(C):
        blocks = []
        for j in range(R):
            if arr[j][i] != '.':
                blocks.append(arr[j][i])
                arr[j][i] = '.'
        
        blocks.reverse()
        for k in range(len(blocks)):
            arr[R-1-k][i] = blocks[k]
        
def BFS(x, y, visited: list):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    q = deque([[x, y, [[x, y]]]])
    visited[x][y] = True

    while q:
        x, y, puyo = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                visited[nx][ny] = True
                puyo.append([nx, ny])
                q.append([nx, ny, puyo])
    
    return puyo if len(puyo) >= 4 else []

R, C = 12, 6
arr = [list(input().rstrip()) for _ in range(R)]
answer = 0

while True:
    flag = find_explode()
    if not flag:
        break
    adjust_block()
    
print(answer)