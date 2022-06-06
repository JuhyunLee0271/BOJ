import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

left, right = 0, 0
answer = sys.maxsize

while left < N and right < N:
    diff = arr[right] - arr[left]
    if diff == M:
        answer = M
        break
    elif diff < M:
        right += 1
    else:
        left += 1
        answer = min(answer, diff)

print(answer)
    