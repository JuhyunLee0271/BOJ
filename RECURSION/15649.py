import sys
input = sys.stdin.readline

def backtracking(tmp_list: list, cnt: int):
    global visited
    if cnt == 0:
        print(*tmp_list)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            tmp_list.append(i)
            
            backtracking(tmp_list, cnt - 1)
            
            visited[i] = False
            tmp_list.pop()  
    return

N, M = map(int, input().split())
visited = [False] * (N+1)
backtracking([], M)

