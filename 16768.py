from collections import deque
import sys
input = sys.stdin.readline

# 붙어있는 블록이 K개 이상일 때 리턴
dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x, y, visited):
    q = deque()
    q.append([x, y, [[x, y]]])
    visited[x][y] = True
    while q:
        x, y, blocks = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                visited[nx][ny] = True
                blocks.append([nx, ny])
                q.append([nx, ny, blocks])

    return blocks if len(blocks) >= K else None

def explode():
    visited = [[False] * M for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                temp = BFS(i, j, visited)
                if temp:
                    result.append(temp)
    
    # 터트릴 것이 없을 때
    if not result:
        return False

    for r in result:
        for x, y in r:
            arr[x][y] = 0
    return True
    
def adjust_block():    
    for y in range(M):
        blocks = []
        for x in range(N):
            if arr[x][y]:
                blocks.append(arr[x][y])
        blocks = [0]*(N-len(blocks)) + blocks
        for k in range(len(blocks)):
            arr[k][y] = blocks[k]

N, K = map(int, input().split())
M = 10
arr = [list(map(int, input().rstrip())) for _ in range(N)]

while True:
    flag = explode()
    adjust_block()
    if not flag:
        break

for i in range(N):
    for j in range(M):
        print(arr[i][j], end='')
    print()
