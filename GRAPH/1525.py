from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
def BFS(start):
    q = deque()
    q.append(start)
    count = dict()
    count[start] = 0
    
    while q:
        now = q.popleft()
        if now == "123456780":
            return count[now]
        
        zero_idx = now.find("0")
        x, y = zero_idx // 3, zero_idx % 3
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                pos = nx*3 + ny
                tmp_list = list(now)
                tmp_list[zero_idx], tmp_list[pos] = tmp_list[pos], tmp_list[zero_idx]
                next = ''.join(tmp_list)
                if next not in count:
                    count[next] = count[now] + 1
                    q.append(next)       
    return -1

target = ""
for _ in range(3):
    a, b, c = map(str, input().split())
    target += (a + b + c)

print(BFS(target))
