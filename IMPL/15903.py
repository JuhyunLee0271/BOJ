import sys, heapq
input = sys.stdin.readline

N,M = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(M):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    heapq.heappush(heap, num1+num2)
    heapq.heappush(heap, num1+num2)
    
print(sum(heap))
