def combination_with_backtracking(start: int, tmp_list: list):
    if len(tmp_list) == K:
        result.append(tmp_list.copy())
        return
    
    for i in range(start, N+1):
        if not visited[i]:
            visited[i] = True
            tmp_list.append(i)
            
            combination_with_backtracking(i, tmp_list)
            
            visited[i] = False
            tmp_list.pop()
    return

def permutation_with_backtracking(tmp_list: list):
    if len(tmp_list) == K:
        result.append(tmp_list.copy())
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            tmp_list.append(i)
            
            permutation_with_backtracking(tmp_list)
            
            visited[i] = False
            tmp_list.pop()
    return

N, K = map(int, input().split())

result, visited = [], [False] * (N+1)
combination_with_backtracking(1, [])
print(result)

result, visited = [], [False] * (N+1)
permutation_with_backtracking([])
print(result)

