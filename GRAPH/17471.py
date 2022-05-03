from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def BFS(pair):
    visited = [False] * (N+1)
    q = deque()
    q.append(pair[0])
    visited[pair[0]] = True
    
    while q:
        x = q.popleft()
        for v in graph[x]:
            if not visited[v] and v in pair:
                q.append(v)
                visited[v] = True
    
    for p in pair:
        if not visited[p]:
            return False
    
    return True
    

N = int(input())
arr = [0] + list(map(int, input().split()))
cost = {i: arr[i] for i in range(N+1)}
graph = [[] for _ in range(N+1)]
answer = sys.maxsize

for i in range(1, N+1):
    conn = list(map(int, input().split()))
    for node in conn[1:]:
        graph[i].append(node)

for i in range(1, N//2+1):
    pairs = list(combinations([i for i in range(1, N+1)], i))
    for pair in pairs:
        cities_1 = list(pair)
        cities_2 = list(set([i for i in range(1, N+1)]) - set(pair))
        if BFS(cities_1) and BFS(cities_2):
            answer = min(answer, abs(sum([cost[i] for i in cities_1]) - sum([cost[i] for i in cities_2])))

print(-1) if answer == sys.maxsize else print(answer)