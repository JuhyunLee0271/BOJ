from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
op = list(input().rstrip().split())

result = []
for p in list(permutations([0,1,2,3,4,5,6,7,8,9], N+1)):
    flag = True
    for i in range(len(p)-1):
        if op[i] == '>' and p[i] < p[i+1]:
            flag = False
            break
        if op[i] == '<' and p[i] > p[i+1]:
            flag = False
            break
    if flag:
        result.append(''.join(map(str, p)))

print(max(result))
print(min(result))