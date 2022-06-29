import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def backtracking(x, y, cur_sum, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, cur_sum)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = True
                backtracking(x, y, cur_sum + arr[nx][ny], cnt + 1)
                visited[nx][ny] = False
            
            visited[nx][ny] = True
            backtracking(nx, ny, cur_sum + arr[nx][ny], cnt + 1)
            visited[nx][ny] = False
    return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        backtracking(i, j, arr[i][j], 1)
        visited[i][j] = False

print(answer)