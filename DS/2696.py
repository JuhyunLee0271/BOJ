from heapq import heappush, heappop
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    numbers = []
    if M % 10 == 0:
        for _ in range(M//10):
            numbers.extend(list(map(int, input().rstrip().split(' '))))
    else:
        for _ in range(M//10+1):
            numbers.extend(list(map(int, input().rstrip().split(' '))))

    left_heap, right_heap = [], []
    answer = []

    for i in range(len(numbers)):
        if len(left_heap) == len(right_heap):
            heappush(left_heap, [-numbers[i],numbers[i]])
        else:
            heappush(right_heap, numbers[i])
        
        if left_heap and right_heap and (left_heap[0][1] > right_heap[0]):
            l_value = heappop(left_heap)[1]
            r_value = heappop(right_heap)
            heappush(left_heap, [-r_value, r_value])
            heappush(right_heap, l_value)
        
        if i % 2 == 0:
            answer.append(left_heap[0][1])

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=' ')
        if (i + 1) % 10 == 0:
            print()
    print()