from itertools import product
import sys
input = sys.stdin.readline

def getButtons(M):
    if M == 0:
        buttons = [i for i in range(10)]
    else:
        temp = list(map(int, input().split()))
        buttons = [i for i in range(10) if i not in temp]
    return buttons

N = int(input())
M = int(input())
length = len(str(N))

cur = 100
answer = abs(N-cur)
buttons = getButtons(M)

for i in range(6, 0, -1):
    for val in product(buttons, repeat=i):
        temp = int(''.join(list(map(str, val))))
        answer = min(answer, len(str(temp)) + abs(temp - N))

print(answer)

        

