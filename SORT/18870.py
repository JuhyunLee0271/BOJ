import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
temp = dict()
for idx, val in enumerate(sorted(list(set(arr)))):
    temp[val] = idx

for num in arr:
    print(temp[num], end=' ')
print()

