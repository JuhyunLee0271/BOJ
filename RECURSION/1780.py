import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check(arr, x, y, length):
    flag = True
    num = arr[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if arr[i][j] != num:
                flag = False
                break
    
    if flag:
        if num == -1: result[0] += 1
        if num == 0: result[1] += 1
        if num == 1: result[2] += 1
    
    else:
        for i in range(x, x + length, length//3):
            for j in range(y, y + length, length//3):
                check(arr, i, j, length//3)
    
    return 
    
N = int(input())
graph = []
result = [0,0,0]
for _ in range(N):
    graph.append(list(map(int, input().split())))

check(graph, 0, 0, N)
for e in result:
    print(e)