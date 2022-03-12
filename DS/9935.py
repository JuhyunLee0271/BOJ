from collections import deque
import sys
input = sys.stdin.readline

S = input().rstrip()
target = input().rstrip()
result = []

for i in range(len(S)):
    result.append(S[i])
    if result[-1] == target[-1] and ''.join(result[-len(target):]) == target:
        del result[-len(target):]
if not result: print("FRULA")
else: print(''.join(result))          