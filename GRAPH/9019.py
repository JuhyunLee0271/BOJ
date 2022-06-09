from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    q = deque()
    q.append([A, ""])  # 현재숫자, 커맨드
    visited = [False] * 10000

    while q:
        current, command = q.popleft()
        if visited[current]:
            continue
        visited[current] = True
        
        if current == B:
            print(command)
            break
        
        # D
        next = 2*current % 10000
        q.append([next, command + "D"])
        
        # S
        next = (current-1) % 10000
        q.append([next, command + "S"])
        
        # L
        next = (10*current+(current//1000))%10000
        q.append([next, command + "L"])
        
        # R
        next = (current//10 + (current%10)*1000)%10000
        q.append([next, command + "R"])
