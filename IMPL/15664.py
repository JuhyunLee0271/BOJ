from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

for e in sorted(list(set(combinations(numbers, M)))):
    print(*e)