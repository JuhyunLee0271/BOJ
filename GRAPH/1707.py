from collections import deque
import sys

input = sys.stdin.readline

def bipartite(arr, colored, visited, start):
    q = deque()
    q.append(start)
    colored[start] = 'B'
    visited[start] = True
    while q:
        v = q.popleft()
        for e in arr[v]:
            if not visited[e] and colored[e] == '0':
                if colored[v] == 'B': colored[e] = 'W'
                elif colored[v] == 'W': colored[e] = 'B'
                q.append(e)
                visited[e] = True
            elif colored[e] == colored[v]:
                return False

    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    arr = []
    for _ in range(V+1):
        arr.append([])
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    colored = ['0'] * (V+1)
    visited = [False] * (V+1)
    for i in range(1, V+1):
        if not visited[i]:
            result = bipartite(arr, colored, visited, i)
            if not result:
                break
    print("YES" if result else "NO")