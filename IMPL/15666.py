from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))
result = set()

for case in combinations_with_replacement(numbers, M):
    if case not in result:
        result.add(case)
        print(*case)

