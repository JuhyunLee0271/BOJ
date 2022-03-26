import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(x):
    global result
    visited[x] = True
    cycle.append(x)
    num = arr[x]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        DFS(num)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    result = []
    
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            DFS(i)
    
    print(N - len(result))