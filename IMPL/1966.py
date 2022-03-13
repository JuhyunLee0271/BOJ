import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    queue = deque(list(enumerate(map(int, input().split()))))
    result = []
    
    while queue:
        value = queue[0][1]
        cond = True
        for i in range(1, len(queue)):
            if queue[i][1] > value:
                queue.append(queue.popleft())
                cond = False
                break
        if cond:
            result.append(queue.popleft())

        if result and result[-1][0] == M:
            break

    print(len(result))