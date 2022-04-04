from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewerly = sorted([list(map(int, input().split())) for _ in range(N)])
bags = sorted([int(input()) for _ in range(K)])

result = 0
heap = []

for bag in bags:
    while jewerly and bag >= jewerly[0][0]:
        heappush(heap, -jewerly[0][1])
        heappop(jewerly)
    
    if heap:
        result += heappop(heap)
    elif not jewerly:
        break

print(-result)