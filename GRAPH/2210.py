from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def DFS(x, y, cnt, string):
    global result
    string += str(graph[x][y])
    cnt += 1
    if cnt == 6:
        result.add(string)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            DFS(nx, ny, cnt, string)

graph = [list(map(int, input().split())) for _ in range(5)]

result = set()
for i in range(5):
    for j in range(5):
        DFS(i, j, 0, '')

print(len(result))
