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

N, M = map(int, input().split())
parents = [i for i in range(0, N)]
answer = 0

for idx, pair in enumerate([list(map(int, input().split())) for _ in range(M)]):
    a, b = pair
    if find(a) == find(b):
        answer = idx + 1
        break
    else:
        union(a, b)

print(answer)