import sys
input = sys.stdin.readline

def check(arr, x, y, length):
    color = arr[x][y]
    flag = True
    for i in range(x, x+length):
        for j in range(y, y+length):
            if arr[i][j] != color:
                flag = False
                break

    # 전부 같은 색일 때
    if flag:
        result[color] += 1
    # 그렇지 않을 때
    else:
        for i in range(x, x+length, length//2):
            for j in range(y, y+length, length//2):
                check(arr, i, j, length//2)
    return

N = int(input())
arr = []
result = [0,0]
for _ in range(N):
    arr.append(list(map(int, input().split())))

check(arr, 0, 0, N)
for e in result:
    print(e)