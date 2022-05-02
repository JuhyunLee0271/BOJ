import sys
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return parent[a]
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: 
        return
    if cost[a] < cost[b]: 
        parent[b] = a
    else:
        parent[a] = b
    
N, M, K = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

friends = set()
for i in range(1, N+1):
    if find(i) not in friends:
        result += cost[parent[i]]
        friends.add(parent[i])

print(result) if K >= result else print("Oh no")