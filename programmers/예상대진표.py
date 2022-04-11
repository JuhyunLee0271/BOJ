import math

def solution(n,a,b):
    answer = 1
    while n > 2:
        a, b = math.ceil(a/2), math.ceil(b/2)
        if a == b: break
        answer += 1
        n /= 2

    return answer