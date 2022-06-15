input = __import__('sys').stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

answer = 10**9

for k in range(N - 7):
    for l in range(M - 7):
        a, b = 0, 0
        for i in range(k, k+8):
            for j in range(l, l+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W': a += 1
                    if arr[i][j] != 'B': b += 1
                else:
                    if arr[i][j] != 'B': a += 1
                    if arr[i][j] != 'W': b += 1
        answer = min(answer, min(a, b))

print(answer)