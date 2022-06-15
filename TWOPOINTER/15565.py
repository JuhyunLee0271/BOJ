import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 10**9
count = 0
left, right = 0, 0
if arr[right] == 1:
    count += 1

while right < N:
    if count == K:
        answer = min(answer, right - left + 1)
        if arr[left] == 1:
            count -= 1
        left += 1
    
    else:
        right += 1
        if right < N and arr[right] == 1:
            count += 1

print(-1) if answer == 10**9 else print(answer)
        