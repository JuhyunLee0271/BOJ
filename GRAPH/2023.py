from collections import deque
import sys
input = sys.stdin.readline

def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def BFS(num):
    q = deque()
    q.append(num)
    while q:
        x = q.popleft()
        if len(str(x)) == N:
            print(x)
        for i in range(10):
            new = 10*x + i
            if isprime(new):
                q.append(new)

N = int(input())
prime = [2, 3, 5, 7]

for p in prime:
    BFS(p)    