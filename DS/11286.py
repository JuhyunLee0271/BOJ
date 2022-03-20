import sys, heapq
input = sys.stdin.readline

N = int(input())
negative_heap = []
positive_heap = []

for _ in range(N):
    command = int(input())
    
    if command == 0:
        if negative_heap and positive_heap:
            negative = heapq.heappop(negative_heap)
            positive = heapq.heappop(positive_heap)
            if abs(negative[1]) > abs(positive):
                heapq.heappush(negative_heap, negative)
                print(positive)
            elif abs(negative[1]) <= abs(positive):
                heapq.heappush(positive_heap, positive)
                print(negative[1])
        
        elif negative_heap:
            negative = heapq.heappop(negative_heap)
            print(negative[1])
        elif positive_heap:
            positive = heapq.heappop(positive_heap)
            print(positive)
        else:
            print(0)
    
    else:
        if command < 0:
            heapq.heappush(negative_heap, (-command, command))
        else:
            heapq.heappush(positive_heap, command)
