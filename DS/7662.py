from heapq import heappush, heappop
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    visited = [False] * 1000001
    min_heap, max_heap = [], []
    answer = []
    for i in range(N):
        comm, num = input().rstrip().split()
        num = int(num)
        
        if comm == "I":
            heappush(min_heap, [num, i])
            heappush(max_heap, [-num, i])
            visited[i] = True
        
        elif comm == "D":
            # 최소값 빼기
            if num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)

            # 최대값 빼기
            elif num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
        
        while min_heap and not visited[min_heap[0][1]]:
            heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heappop(max_heap)
        
    if min_heap and max_heap: 
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")