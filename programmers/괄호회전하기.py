def iscorrect(s):
    stack = []
    for b in s:
        if b in ['(', '[', '{']:
            stack.append(b)
        else:
            if stack:
                if b == ']' and stack[-1] == '[':
                    stack.pop()
                elif b == '}' and stack[-1] == '{':
                    stack.pop()
                elif b == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)
            
    return True if not stack else False


def solution(s):
    answer = 0
    for i in range(len(s)):
        if iscorrect(s[i:] + s[:i]):
            answer += 1
    return answer