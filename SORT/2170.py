import sys
input = sys.stdin.readline

N = int(input())
lines = []
answer = 0
numbers = [list(map(int, input().split())) for _ in range(N)]

for a, b in sorted(numbers, key=lambda x:x[0]):
    if not lines:
        lines = [a, b]
    if lines[0] <= a <= lines[1] and lines[0] <= b <= lines[1]:
        continue
    if a <= lines[1] and b >= lines[1]:
        lines = [lines[0], b]
    else:
        answer += (lines[1] - lines[0])
        lines = [a, b]
if lines:
    answer += (lines[1] - lines[0])
print(answer)