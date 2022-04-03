from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
jobs = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
queue = []

for cost, deadline in jobs:
    heappush(queue, cost)
    if len(queue) > deadline:
        heappop(queue)

print(sum(queue))