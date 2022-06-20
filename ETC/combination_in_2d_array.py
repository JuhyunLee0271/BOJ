import sys
input = sys.stdin.readline

def combination_with_backtracking(start: int, tmp_list: list, cnt: int):
    if len(tmp_list) == cnt:
        result.append(tmp_list.copy())
        return
    
    for i in range(start, N*M):
        if not visited[i] and i in candidate:
            visited[i] = True
            tmp_list.append(linear_to_array(i))
            
            combination_with_backtracking(i, tmp_list, cnt)
            
            visited[i] = False
            tmp_list.pop()
            
    return

# pos -> (x, y)
def linear_to_array(pos):
    return [pos // M, pos % M]

# (x, y) -> pos
def array_to_linear(x, y):
    return x*M+y

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*N*M

candidate = [array_to_linear(x, y) for x in range(N) for y in range(M) if arr[x][y] == 0]
result = []
combination_with_backtracking(0, [], K)
print(result)