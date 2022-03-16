import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

cond = 0
while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if T == S:
        cond = 1
        break
print(cond)