import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

low, high = 1, max(lines)

while low <= high:
    mid = (low+high) // 2
    num = 0
    for line in lines:
        num += line // mid
    if num >= N:
        low = mid + 1
    elif num < N:
        high = mid - 1

print(high)

