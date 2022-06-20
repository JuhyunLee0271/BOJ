import sys
input = sys.stdin.readline

def backtracking(player, total):
    global answer, visited
    if player == 11:
        answer = max(answer, total)
        return

    for i in range(11):
        if arr[player][i] != 0 and not visited[i]:
            total += arr[player][i]
            visited[i] = True
            
            backtracking(player + 1, total)
            
            total -= arr[player][i]
            visited[i] = False            
    return
    
for _ in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    answer = 0
    backtracking(0, 0)
    print(answer)

