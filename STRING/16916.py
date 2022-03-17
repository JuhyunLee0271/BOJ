import sys
input = sys.stdin.readline

P = input().rstrip()
S = input().rstrip()

pi = [0] * (len(S))
idx = 0

for i in range(1, len(S)):
    while idx > 0 and S[i] != S[idx]:
        idx = pi[idx-1]
    if S[i] == S[idx]:
        idx += 1
        pi[i] = idx

idx = 0
cond = 0
for i in range(0, len(P)):
    while idx > 0 and P[i] != S[idx]:
        idx = pi[idx-1]
    if P[i] == S[idx]:
        if idx == len(S) - 1:
            cond = 1
            break
        else:
            idx += 1
print(cond)