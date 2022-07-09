from collections import deque
from itertools import combinations

N, M = 5, 5
dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(x1, y1, x2, y2, arr):
    global N, M
    q = deque()
    q.append([x1, y1, 0])
    visited = [[False] * M for _ in range(N)]
    visited[x1][y1] = True
    
    while q:
        x, y, dist = q.popleft()
        if x == x2 and y == y2:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append([nx, ny, dist + 1])
    
    if not visited[x2][y2]:
        return True
    return False if dist <= 2 else True

def solution(places):
    global N, M
    answer = []
    arr = [[[] for _ in range(M)] for _ in range(N)]
    for place in places:
        for i in range(N):
            for j in range(M):
                arr[i][j] = place[i][j]
        people = [[i, j] for i in range(N) for j in range(M) if arr[i][j] == 'P']
        flag = True
        for p1, p2 in combinations(people, 2):
            x1, y1 = p1
            x2, y2 = p2
            flag = BFS(x1, y1, x2, y2, arr)
            if not flag:
                break
        if flag: 
            answer.append(1)
        else:
            answer.append(0)
    return answer