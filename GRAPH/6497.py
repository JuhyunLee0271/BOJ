from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return parents[x]
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return 
    elif x < y: parents[y] = x
    else: parents[x] = y

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    parents = [i for i in range(M)]
    heap = []
    MST = 0
    
    for _ in range(N):
        x, y, z = map(int, input().split())
        MST += z
        heappush(heap, [z, x, y])
            
    cnt = 0
    while heap:
        if cnt == M-1:
            break
        weight, src, dst = heappop(heap)
        if find(src) != find(dst):
            union(src, dst)
            MST -= weight
            cnt += 1
            
    print(MST)