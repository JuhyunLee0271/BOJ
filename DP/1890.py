import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        
        down = i + graph[i][j] 
        right = j + graph[i][j]
        
        if 0 <= down < N:
            dp[down][j] += dp[i][j]
        if 0 <= right < N:
            dp[i][right] += dp[i][j]

print(dp[-1][-1])