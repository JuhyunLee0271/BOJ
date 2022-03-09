import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().rstrip('\n'))

result = 0
for _ in range(M):
    target = input().rstrip('\n')
    for e in arr:
        if target == e[:len(target)]:
            result += 1
            break
print(result)