import sys
input = sys.stdin.readline
INF = sys.maxsize

def DFS(x):
    for v in tree[x]:
        DFS(v)
    tree[x] = INF

N = int(input())
tree = [[]*N for _ in range(N)]
edges = list(map(int, input().split()))    
K = int(input())
for idx, node in enumerate(edges):
    if node == -1: continue
    tree[node].append(idx)
DFS(K)
try:
    tree[edges[K]].remove(K)
except:
    pass
result = 0
for node in tree:
    if not node: 
        result += 1
print(result)
