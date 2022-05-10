import sys
input = sys.stdin.readline

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input())
numbers = [i for i in range(N+1) if isprime(i)]
answer = 0
if N == 1:
    print(0)
else:
    # two pointer
    start, end = 0, 1
    current_sum = numbers[start] + numbers[end]
    while start < len(numbers)-1 and end < len(numbers)-1:
        if current_sum < N:
            end += 1
            current_sum += numbers[end]
        elif current_sum > N:
            current_sum -= numbers[start]
            start += 1
        else:
            current_sum -= numbers[start]
            start += 1
            end += 1
            current_sum += numbers[end]
            answer += 1

    if isprime(N): answer += 1
    print(answer)