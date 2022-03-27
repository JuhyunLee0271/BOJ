import sys
input = sys.stdin.readline

N, C = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()

# Gap
start = 1
end = numbers[-1] - numbers[0]

while start <= end:
    mid = (start + end) // 2
    val, count = numbers[0], 1
    for i in range(1, len(numbers)):
        if numbers[i] >= val + mid:
            count += 1
            val = numbers[i]
    if count >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)
