from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
lecture = []
for _ in range(N):
    a, b = map(int, input().split())
    lecture.append([a, b])
lecture.sort()

heap = []
heappush(heap, lecture[0][1])

for i in range(1, N):
    if lecture[i][0] < heap[0]:
        heappush(heap, lecture[i][1])
    else:
        heappop(heap)
        heappush(heap, lecture[i][1])

print(len(heap))