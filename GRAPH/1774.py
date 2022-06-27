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
parents = [i for i in range(N+1)]
pos = [[]]
roads = []
cnt = 0
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    pos.append([x, y])

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
    cnt += 1

for i in range(1, N):
    for j in range(i+1, N+1):
        distance = ((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)**0.5
        roads.append([distance, i, j])

roads.sort(key=lambda x:x[0])

for dist, a, b in roads:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        answer += dist
    if cnt == N-1:
        break

print(f"{answer:.2f}")
    

