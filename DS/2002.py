N = int(input())
arr = dict()
out = []
result = 0

for i in range(N):
    arr[input()] = i

for i in range(N):
    out.append(input())

for i in range(N):
    for j in range(i+1, N):
        if arr[out[i]] > arr[out[j]]:
            result += 1
            break
print(result)


