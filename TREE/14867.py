import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return parents[x]
    parents[x] = find(parents[x])
    return parents[x]
    
def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    elif a < b: parents[b] = a
    else: parents[a] = b

def convert_to_linear(x, y):
    return M*x + y

def DFS(x, y):
    if visited[x][y]:
        return
    visited[x][y] = True
    nx, ny = x + way[graph[x][y]][0], y + way[graph[x][y]][1]
    pos_1, pos_2 = convert_to_linear(x, y), convert_to_linear(nx, ny)
    union(pos_1, pos_2)
    DFS(nx, ny)
    
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
way = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
parents = [k for k in range(N*M)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            DFS(i,j)

disjoint = set()
for node in parents[1:]:
    disjoint.add(find(node))

print(len(disjoint))

