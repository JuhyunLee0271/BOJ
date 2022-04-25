from collections import deque
import sys
input = sys.stdin.readline

def compare(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

N, M = map(int, input().split())
A = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
B = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
answer = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            compare(i, j)
            answer += 1
     
print(answer) if check() else print(-1)