import sys
input = sys.stdin.readline

s = list(input().rstrip())
stack = []
result = ""
op = []

for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        result += s[i]
    else:
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                result += stack.pop()
            stack.append(s[i])
        elif s[i] in ['+', '-']:
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(s[i])
        elif s[i] == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)
    
    
