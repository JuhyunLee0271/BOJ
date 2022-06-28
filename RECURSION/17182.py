import sys
input = sys.stdin.readline

def backtracking(current_node: int, current_sum: int, cnt: int):
    global answer
    
    if cnt == N:
        answer = min(answer, current_sum)
        return
    
    for node in range(N):
        if not visited[node]:
            visited[node] = True
            backtracking(node, current_sum + arr[current_node][node], cnt + 1)
            visited[node] = False

    return

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 1e9

for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

visited = [False] * N
visited[K] = True
backtracking(K, 0, 1)
print(answer)