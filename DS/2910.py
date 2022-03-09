import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))
numbers = dict()

for e in arr:
    if e not in numbers:
        numbers[e] = 1
    else:
        numbers[e] += 1

for val, cnt in list(sorted(numbers.items(), key=lambda x:-x[1])):
    for _ in range(cnt):
        print(val, end=' ')



    
