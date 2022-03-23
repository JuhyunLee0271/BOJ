import sys
input = sys.stdin.readline

strings = list(input().rstrip())
stack = []
result = 0

for i in range(len(strings)):
    if strings[i] == '(':
        stack.append(strings[i])
    if strings[i] == ')' and strings[i-1] == '(':
        stack.pop()
        result += len(stack)
    if strings[i] == ')' and strings[i-1] == ')' and stack[-1] == '(':
        stack.pop()
        result += 1

print(result)