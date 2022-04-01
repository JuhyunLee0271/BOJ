import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        a, b = map(int, input().split())
        score.append([a,b])
    score.sort(key=lambda x:x[0])
    
    result = 1
    value = score[0][1]
    for i in range(1, N):
        if value > score[i][1]:
            value = score[i][1]
            result += 1
    print(result)
