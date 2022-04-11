def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
    
    while k > 0:
        stack.pop()
        k -= 1

    answer = ''.join(stack)
    return answer