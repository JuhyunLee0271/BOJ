import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    answer = []
    diff = 10**9
    left, right = 0, N-1

    while left < right:
        _sum = arr[left] + arr[right]
        if abs(_sum - K) < diff:
            answer = []
            answer.append([arr[left], arr[right]])
            diff = abs(_sum - K)
        elif abs(_sum - K) == diff:
            answer.append([arr[left], arr[right]])
        
        if _sum > K:
            right -= 1
        else:
            left += 1

    print(len(answer))