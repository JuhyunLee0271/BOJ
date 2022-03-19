from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
prod = list(permutations(numbers, len(numbers)))
result = 0

for nums in prod:
    temp = 0
    for i in range(0, N-1):
        temp += abs(nums[i] - nums[i+1])
    result = max(result, temp)
print(result)

