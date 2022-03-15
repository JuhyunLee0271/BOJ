import sys
input = sys.stdin.readline

N = int(input())
result = 0
for _ in range(N):
    stack = []
    string = list(input().rstrip())
    
    for i in range(len(string)):
        stack.append(string[i])
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if not stack:
        result += 1
print(result)