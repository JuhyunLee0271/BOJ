import sys, heapq
input = sys.stdin.readline

left_heap = []
right_heap = []

N = int(input())
for _ in range(N):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, num)

    if right_heap and left_heap[0][1] > right_heap[0]:
        a = heapq.heappop(left_heap)
        b = heapq.heappop(right_heap)

        heapq.heappush(right_heap, a[1])
        heapq.heappush(left_heap, (-b, b))
    
    print(left_heap[0][1])
    