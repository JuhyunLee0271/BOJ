import sys
input = sys.stdin.readline

def findPath(node):
    result = []
    while node != parents[node]:
        result.append(node)
        node = parents[node]
    result.append(node)
    return result[::-1]

def solution(path1, path2):
    if len(path1) == 1 or len(path2) == 1:
        return path1[0]

    if len(path1) <= len(path2):
        s, l = path1, path2
    else:
        s, l = path2, path1
    
    cond = False
    for i in range(1, len(s)):
        if s[i] != l[i]:
            cond = True
            break
    if cond: return s[i-1]
    else: return s[i]

T = int(input())
for _ in range(T):
    N = int(input())
    parents = [i for i in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        parents[b] = a
    a, b = map(int, input().split())
    print(solution(findPath(a), findPath(b)))