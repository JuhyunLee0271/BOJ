from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check_cycle(node, target, visited, temp):
    visited[node] = True
    for v in graph[node]:
        if not visited[v]:
            check_cycle(v, target, visited, temp)
        elif visited[v] and v == target:
            temp.append(True)
    return temp

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
cond = False

for _ in range(M):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)-1):
        graph[arr[j]].append(arr[j+1])
        indegree[arr[j+1]] += 1

for i in range(1, N+1):
    if check_cycle(i, i, [False] * (N+1), []):
        cond = True
        break

if not cond:
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        x = q.popleft()
        result.append(x)
        for v in graph[x]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    for e in result:
        print(e)
    
else:
    print(0)