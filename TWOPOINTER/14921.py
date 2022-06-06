import sys
input = sys.stdin.readline

N = int(input())
criteria = 0
arr = list(map(int, input().split()))

left, right = 0, N-1
answer = arr[left] + arr[right]

while left < right:
    tmp = arr[left] + arr[right]
    if abs(answer) > abs(tmp):
        answer = tmp
    if tmp < criteria:
        left += 1
    else:
        right -=1

print(answer)