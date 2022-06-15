from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 10**9

for p in permutations([i for i in range(2, N+1)], N-1):
    cost = 0
    path = [1] + list(p) + [1]
    for i in range(len(path)-1):
        _cost = arr[path[i]-1][path[i+1]-1]
        if _cost == 0: _cost = 10**9
        cost += _cost
    answer = min(answer, cost)
    
print(answer)