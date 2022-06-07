import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
cur_max = 0
answer = 0

for i in range(N-1, -1, -1):
    if arr[i] > cur_max:
        cur_max = arr[i]
        answer += 1
    
print(answer)