import sys
input = sys.stdin.readline

def check(path):
    flag = True
    for i in range(len(path)-1):
        if arr[path[i]-1][path[i+1]-1] == 0:
            flag = False
            break
    return "YES" if flag else "NO"

N = int(input())
M = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                arr[i][j] = 1
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

path = list(map(int, input().split()))
print(check(path))