import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().rstrip()))
stack = []
count = 0

for i in range(len(numbers)):
    while stack and stack[-1] < numbers[i] and count < K:
        stack.pop()
        count += 1
    stack.append(numbers[i])

if count < K:
    stack = stack[:-(K-count)]

for e in stack:
    print(e, end='')


