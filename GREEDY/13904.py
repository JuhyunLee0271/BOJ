import sys
input = sys.stdin.readline

def feasible(arr):
    arr.sort()
    for i in range(len(arr)):
        if i + 1 > arr[i]:
            return False
    return True

N = int(input())
jobs = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: -x[1])
result = 0
queue = []

for deadline, cost in jobs:
    if feasible(queue + [deadline]):
        queue.append(deadline)
        result += cost

print(result)