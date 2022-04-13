import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = sys.maxsize

dp = [[0] * 3 for _ in range(N)]
answer = INF

# 한 집을 빼고 모두 INF로 변경해 강제적으로 그 집을 선택하도록 함
for k in range(3):
    dp[0][0] = dp[0][1] = dp[0][2] = INF
    dp[0][k] = arr[0][k]
    
    for i in range(1, N):
        for j in range(3):
            dp[i][j] = min(dp[i-1][:j] + dp[i-1][j+1:]) + arr[i][j]
        
    answer = min(answer, min(dp[-1][:k] + dp[-1][k+1:]))

print(answer)