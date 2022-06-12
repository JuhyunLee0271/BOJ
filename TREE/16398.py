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

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N+1)]
heap = [] # [cost, src, dst]

for i in range(N):
    for j in range(i+1, N):
        heappush(heap, [graph[i][j], i, j])

cnt = 0
answer = 0
while heap:
    if cnt == N-1:
        break
    cost, src, dst = heappop(heap)
    if find(src) != find(dst):
        union(src, dst)
        answer += cost
        cnt += 1

print(answer)
