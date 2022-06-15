import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

answer = 0
left, right = 0, 0

alpha = dict()
alpha[S[0]] = 1

while left < len(S) and right < len(S):
    if len(alpha.items()) <= N:
        answer = max(answer, right - left + 1)
        right += 1
        if right < len(S):
            if S[right] in alpha:
                alpha[S[right]] += 1
            else:
                alpha[S[right]] = 1
    else:
        alpha[S[left]] -= 1
        if alpha[S[left]] == 0:
            del alpha[S[left]]
        left += 1

print(answer)
        
    
    
    