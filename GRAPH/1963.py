from collections import deque
import sys
input = sys.stdin.readline

def BFS(src, dst):
    q = deque()
    q.append((src, 0))

    while q:
        now, cnt = q.popleft()
        if now == dst:
            return cnt
        strNow = str(now)
        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])
                if not visited[temp] and temp in primes:
                    visited[temp] = True
                    q.append((temp, cnt + 1))
    
def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

primes = [i for i in range(1000, 10000) if isprime(i)]

T = int(input())
for _ in range(T):
    src, dst = map(int, input().split())
    visited = [False] * 10001
    visited[src] = True
    res = BFS(src, dst)
    print("Impossible") if res == None else print(res)    