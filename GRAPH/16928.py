from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [0] * 101
visited = [False] * 101
ladder = dict()
snake = dict()
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in range(1, 6+1):
        nx = x + i
        if 0 <= nx < 101 and not visited[nx]:
            if nx in ladder:
                nx = ladder[nx]
            if nx in snake:
                nx = snake[nx]
            if not visited[nx]:
                cost[nx] = cost[x] + 1
                visited[nx] = True
                q.append(nx)

print(cost[100])            