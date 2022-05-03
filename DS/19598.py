from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
meeting = []
heap = []
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append([a, b])

meeting.sort(key=lambda x:x[0])

for start, end in meeting:
    if heap and heap[0][0] <= start:
        heappop(heap)
        heappush(heap, [end, start])
    else:
        heappush(heap, [end, start])

print(len(heap))