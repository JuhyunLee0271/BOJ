import sys
input = sys.stdin.readline

N = int(input())
pos = []
neg = []

for _ in range(N):
    num = int(input())
    if num > 0: pos.append(num)
    else: neg.append(num)

pos.sort(reverse=True)
neg.sort()

result = 0

temp = 0
# For positive number
for i in range(len(pos)):
    if i%2 == 0: 
        temp += pos[i]
        if i == len(pos)-1:
            result += temp
    else: 
        if pos[i] == 1: 
            temp += pos[i]
        else: 
            temp *= pos[i]
        result += temp
        temp = 0

temp = 0
# For negative number
for i in range(len(neg)):
    if i%2 == 0:
        temp += neg[i]
        if i == len(neg)-1:
            result += temp
    else:
        temp *= neg[i]
        result += temp
        temp = 0

print(result)