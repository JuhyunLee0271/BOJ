import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
answer = [0] * (N+1)
stack = []

for i in range(N, 0, -1):
    while stack and stack[-1][1] < numbers[i]:
        idx, val = stack.pop()
        answer[idx] = i
    stack.append((i, numbers[i]))

print(*answer[1:])
