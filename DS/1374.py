from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
lessons = []
heap = []

for _ in range(N):
    a, b, c = map(int, input().split())
    lessons.append([b,c])

lessons.sort(key=lambda x:x[0])

# heap: [end, start]
for start, end in lessons:
    if heap and heap[0][0] <= start:
        heappop(heap)
        heappush(heap, [end, start])
    else:
        heappush(heap, [end, start])

print(len(heap))

    