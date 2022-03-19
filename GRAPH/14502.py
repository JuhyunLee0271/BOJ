from collections import deque
from itertools import combinations
import sys, copy
input = sys.stdin.readline

def BFS(arr, starts):
    result = 0

    q = deque()
    for i in range(len(starts)):
        q.append(starts[i])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = -1
                q.append((nx, ny))
    
    for e in arr:
        result += e.count(0)
    return result

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

virus = []
pair = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            pair.append((i,j))

pairs = list(combinations(pair, 3))
result = 0

for a,b,c in pairs:
    arr_copy = copy.deepcopy(arr)
    arr_copy[a[0]][a[1]] = 1;   arr_copy[b[0]][b[1]] = 1;   arr_copy[c[0]][c[1]] = 1
    result = max(result, BFS(arr_copy, virus))

print(result)