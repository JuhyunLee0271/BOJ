import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check(string):
    for idx in range(1, len(string)//2+1):
        if string[-idx:] == string[-2*idx:-idx]:
            return False
    return True
    

def backtracking(current: list, idx: int):
    if len(current) == N:
        print(current)
        sys.exit()
    
    for i in range(1, 3+1):
        temp_string = current + str(i)
        if check(temp_string):
            backtracking(temp_string, idx + 1)
    return

N = int(input())
backtracking('1', 1)