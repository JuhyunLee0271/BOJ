def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    for a, b in results:
        graph[b][a] = 1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1
    
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if graph[i][j] == 1 or graph[j][i] == 1:
                cnt += 1
        if cnt == n - 1:
            answer += 1
    
    return answer