import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
stack = []
answer = [-1]*N

for i in range(len(numbers)):
    while stack and stack[-1][1] < numbers[i]:
        idx, val = stack.pop()
        answer[idx] = numbers[i]
    stack.append((i,numbers[i]))

print(*answer)
