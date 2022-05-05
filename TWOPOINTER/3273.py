import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

K = int(input())

start, end = 0, N-1
answer = 0

while start < end:
    if numbers[start] + numbers[end] == K:
        answer += 1
        start += 1
        end -= 1
    elif numbers[start] + numbers[end] < K:
        start += 1
    elif numbers[start] + numbers[end] > K:
        end -= 1
    
print(answer)
    