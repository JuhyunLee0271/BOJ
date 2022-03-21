import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
dx, dy = [-1,1,0,0], [0,0,-1,1]

def BFS(x,y):
    heap = []
    heapq.heappush(heap, (0, x, y))
    dp[0][0] = arr[0][0]

    while heap:
        cost, x, y = heapq.heappop(heap)
        if dp[x][y] < cost:
            continue        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and dp[nx][ny] == INF:
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + arr[nx][ny])
                heapq.heappush(heap, (dp[nx][ny], nx, ny))
    
    return dp[-1][-1]

i = 0
while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = []
        for _ in range(N):
            arr.append(list(map(int, input().split())))
        dp = [[INF]*N for _ in range(N)]

        print(F"Problem {i+1}: {BFS(0,0)}")
        i += 1

