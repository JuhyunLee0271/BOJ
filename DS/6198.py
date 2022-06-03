import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
answer = 0
stack = []

for i in range(len(arr)):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    stack.append(arr[i])
    answer += len(stack) - 1

print(answer)