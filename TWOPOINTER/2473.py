import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

cur_min = sys.maxsize
answer = []

for i in range(N-2):
    cur = arr[i]
    left, right = i+1, N-1
    while left < right:
        cur_sum = cur + arr[left] + arr[right]
        if abs(cur_sum) <= abs(cur_min):
            answer = [cur, arr[left], arr[right]]
            cur_min = cur_sum
        if cur_sum < 0:
            left += 1
        elif cur_sum > 0:
            right -=1
        else:
            print(*answer)
            sys.exit()

print(*answer)