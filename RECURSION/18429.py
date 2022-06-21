import sys
input = sys.stdin.readline


def check(num_list: list):
    target, cur = 500, 500
    for num in num_list:
        cur = cur + kit[num] - K
        if cur < target:
            return False
    return True

def backtracking(current = []):
    global answer
    if len(current) == N:
        if check(current):
            answer += 1
            return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            current.append(i)
            
            backtracking(current)
            
            visited[i] = False
            current.pop()
    return

N, K = map(int, input().split())
kit = list(map(int, input().split()))
visited = [False] * N
answer = 0
backtracking()
print(answer)
