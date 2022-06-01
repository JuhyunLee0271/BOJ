from collections import deque
import sys
input = sys.stdin.readline

def check_distance(c1, c2):
    cnt = 0
    for i in range(K):
        if c1[i] != c2[i]:
            cnt += 1
        if cnt >= 2:
            return False
    return True

def BFS(start, end):
    q = deque()
    q.append([start])
    visited = [False] * (N+1)
    visited[start] = True
    
    while q:
        path = q.popleft()
        if path[-1] == end:
            return path
        for i in range(1, N+1):
            if not visited[i] and check_distance(code[int(path[-1])], str(code[i])):
                visited[i] = True
                q.append(path + [i])
    return -1
    
N, K = map(int, input().split())
code = {i: input().rstrip() for i in range(1, N+1)}
start, end = map(int, input().split())

result = BFS(start, end)
print(-1) if result == -1 else print(*result)
