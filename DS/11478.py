S = input()
len = len(S)
sub = dict()

for i in range(len):
    for j in range(i, len):
        if S[i:j+1] not in sub:
            sub[S[i:j+1]] = 1
            
print(sum(sub.values()))

