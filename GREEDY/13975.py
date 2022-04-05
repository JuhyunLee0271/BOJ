from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    heapify(arr)

    result = 0 
    while len(arr) >= 2:
        a = heappop(arr)
        b = heappop(arr)
        heappush(arr, a+b)
        result += (a+b)

    print(result)