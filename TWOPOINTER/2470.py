import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = N-1

val = INF
result = []

while left < right:
    l_val = numbers[left]
    r_val = numbers[right]

    sum = l_val + r_val
    if abs(sum) < val:
        val = abs(sum)
        result = [l_val, r_val]
    
    if sum < 0:
        left += 1
    else:
        right -=1

print(*result)