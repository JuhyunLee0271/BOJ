import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
answer = 0

while left + 1 < right:
    answer = max(answer, (right - left - 1) * min(arr[left], arr[right]))
    if arr[left] < arr[right]: left += 1
    else: right -= 1
    
print(answer)