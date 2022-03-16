import sys
input = sys.stdin.readline

s = list(input().rstrip())
compress = []

start = s[0]
compress.append(s[0])
for i in range(1, len(s)):
    if s[i] != start: 
        start = s[i]
        compress.append(s[i])
print(min(compress.count('1'), compress.count('0')))

