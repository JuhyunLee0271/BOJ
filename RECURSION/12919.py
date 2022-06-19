import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def backtracking(src: str, dst: str):
    if len(src) == len(dst):
        if src == dst:
            print(1)
            sys.exit()
        else:
            return
    
    if dst[0] == 'B':
        backtracking(src, dst[::-1][:-1])
    if dst[-1] == 'A':
        backtracking(src, dst[:-1])    

S, T = input().rstrip(), input().rstrip()
backtracking(S, T)
print(0)