from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
target = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])

result = 0
for t in target:
    while True:
        if queue[0] == t:
            queue.popleft()
            break
        elif queue.index(t) <= len(queue) // 2:
            queue.append(queue.popleft())
            result += 1
        else:
            queue.appendleft(queue.pop())
            result += 1
print(result)