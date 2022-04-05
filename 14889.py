from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
pair = list(combinations([i for i in range(N)], N//2))
players = [i for i in range(N)]

result = sys.maxsize
for p1 in pair:
    start, link = 0, 0
    p2 = list(set(players) - set(p1))
    for a, b in list(combinations(list(p1), 2)):
        start += arr[a][b]
        start += arr[b][a]
    for a, b in list(combinations(p2, 2)):
        link += arr[a][b]
        link += arr[b][a]
    result = min(result, abs(start-link))

print(result)
    
