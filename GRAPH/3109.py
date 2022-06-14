import sys
input = sys.stdin.readline

dx, dy = [-1, 0, 1], [1, 1, 1]
def DFS(x, y):
    if y == C - 1:
        return True
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C) and not visited[nx][ny] and arr[nx][ny] == '.':
            visited[nx][ny] = True
            if DFS(nx, ny):
                return True
    return False
                 
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
answer = 0

for i in range(R):
    if DFS(i, 0):
        answer += 1

print(answer)