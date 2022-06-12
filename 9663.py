import sys
input = sys.stdin.readline

N = int(input())

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True

def DFS(x):
    global res
    if x == N:
        res += 1
        return
    for i in range(N):
        col[x] = i
        if check(x):
            DFS(x+1)

res = 0
col = [0]*15

DFS(0)
print(res)
        