import sys
input = sys.stdin.readline

def backtracking(current: list, _sum = 0):
    global answer
    if len(current) == 2:
        answer = max(answer, _sum)
        return
    
    for i in range(1, len(current)-1):
        temp = current[i-1] * current[i+1]
        value = current[i]
        del current[i]
        
        backtracking(current, _sum + temp)
        
        current.insert(i, value)
    
    return

N = int(input())
arr = list(map(int, input().split()))
answer = 0
backtracking(arr)
print(answer)