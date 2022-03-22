import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())

chars = dict()

for word in words:
    for char in word:
        chars[char] = 0

for word in words:
    for i in range(len(word)):
        exp = len(word) - i - 1
        chars[word[i]] += pow(10, exp)

char_val = dict()
max_val = 9
for char, val in sorted(list(chars.items()), key=lambda x: -x[1]):
    char_val[char] = max_val
    max_val -= 1

result = 0
for word in words:
    temp = ""
    for char in word:
        temp += str(char_val[char])
    result += int(temp)

print(result)