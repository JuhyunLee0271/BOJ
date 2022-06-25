import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def backtracking(current_string = "", current_sum = 0):
    global result
    if current_sum > N:
        return
    
    if current_sum == N:
        result.append(current_string)
        return
    
    for num in [1, 2, 3]:
        backtracking(current_string=current_string + str(num) + '+', current_sum=current_sum + num)
    

N, K = map(int, input().split())
result = []
backtracking()
print(result[K-1][:-1]) if K - 1 < len(result) else print(-1)
