import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(len(arr)-2):
        answer = max(answer, abs(arr[i+2] - arr[i]))
    print(answer)
