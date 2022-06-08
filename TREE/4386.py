from heapq import heappush, heappop
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

def distances(a, b):
    return ((pos[a][0] - pos[b][0])**2 + (pos[a][1] - pos[b][1])**2)**0.5

N = int(input())
parents = [i for i in range(N+1)]
pos = {i+1: list(map(float, input().split())) for i in range(N)}

heap = []

for i in range(N):
    for j in range(i+1, N):
        heappush(heap, [distances(i+1, j+1), i+1, j+1])

cnt, answer = 0, 0
while heap:
    if cnt == N-1:
        break
    dist, src, dst = heappop(heap)
    if find(src) != find(dst):
        union(src, dst)
        answer += dist
        cnt += 1

print(answer)
        