from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
files = []
for _ in range(N):
    files.append(input().strip('\n').split('.')[1])

for _format, cnt in sorted(list(Counter(files).items()), key=lambda x:x[0]):
    print(_format, cnt)
    