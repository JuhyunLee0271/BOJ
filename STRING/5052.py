import sys
input = sys.stdin.readline

def compare(s1, s2):
    length = len(s1)
    for i in range(len(s2) - length):
        if s2[i:i+length] == s1:
            return True
    return False

T = int(input())
for _ in range(T):
    cond = False
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(input().rstrip())

    numbers.sort()

    for i in range(N-1):
        if compare(numbers[i], numbers[i+1]):
            cond = True
            break
    print("NO") if cond else print("YES")
