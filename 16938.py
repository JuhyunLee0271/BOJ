from itertools import combinations
import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

for k in range(2, N+1):
    for combi in combinations(arr, k):
        if L <= sum(combi) <= R and max(combi) - min(combi) >= X:
            answer.append(combi)

print(len(answer))
    
    