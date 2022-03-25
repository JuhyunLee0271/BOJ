import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1

target = sys.maxsize
result = []
while left < right:
    left_val, right_val = arr[left], arr[right]
    
    if abs(left_val + right_val) <= target:
        target = abs(left_val + right_val)
        result = [left_val, right_val]
    
    if left_val + right_val < 0:
        left += 1
    else:
        right -=1

print(*result)