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
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
K = list(map(int, input().split()))

parties = []
# union, find 
for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(party[1:])
    for i in range(1, len(party)-1):
        if find(party[i]) != find(party[i+1]):
            union(party[i], party[i+1])

if len(K) == 1:
    print(M)
else:
    count = 0
    for party in parties:
        cond = True
        for people in party:
            for target in K[1:]:
                if find(people) == find(target):
                    cond = False
                    break
            if not cond:
                break
        if cond:
            count += 1
    print(count)    