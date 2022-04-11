from collections import deque

def compare(a, b):
    target = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            target += 1
    return False if target > 1 else True
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    
    while q:
        string, cnt = q.popleft()
        if string == target:
            return cnt
        for word in words:
            if compare(string, word) and not visited[words.index(word)]:
                q.append((word, cnt + 1))
                visited[words.index(word)] = True