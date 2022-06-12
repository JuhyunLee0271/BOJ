from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        return find(parents[x])
    return x
    
def union(a, b):
    a, b = find(a), find(b)
    if a < b: parents[b] = a
    else: parents[a] = b
    

N, M, K = map(int, input().split())
parents = [0] * (N+1)
plant = list(map(int, input().split()))
heap = []

for i in range(1, N+1):
    if i not in plant:
        parents[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    heappush(heap, [c, a, b]) # [weight, src, dst]

answer = 0
while heap:
    weight, src, dst = heappop(heap)
    p_src, p_dst = find(src), find(dst)
    if p_src != p_dst:
        union(src, dst)
        answer += weight
    
print(answer)
