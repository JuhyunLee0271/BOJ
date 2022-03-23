import sys
input = sys.stdin.readline

def check(arr, x, y, length):
    global result
    color = arr[x][y]
    flag = True
    for i in range(x, x+length):
        for j in range(y, y+length):
            if arr[i][j] != color:
                flag = False
                break
    
    # 모두 다 같은 색일 때
    if flag:
        result += str(color)
    # 그렇지 않을 때
    else:
        result += '('
        for i in range(x, x+length, length//2):
            for j in range(y, y+length, length//2):
                check(arr, i, j, length//2)
        result += ')'
      
    return

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip())))
result = ""
check(arr, 0, 0, N)
print(result)