import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [sys.maxsize]*2

# 높이
for k in range(0, 256 + 1):
    min_val, max_val = 0, 0
    for i in range(N):
        for j in range(M):
            # 인벤토리에서 꺼내어서 추가
            if arr[i][j] < k:
                min_val += (k - arr[i][j])
            # 블록을 제거하여 인벤토리에 추가 
            else:
                max_val += (arr[i][j] - k)
    
    inventory = max_val + B
    if inventory >= min_val:
        time = max_val*2 + min_val
        if time <= answer[0]:
            answer = [time, k]

print(*answer)  
    
    