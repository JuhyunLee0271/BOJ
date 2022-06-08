from itertools import combinations
import sys
input = sys.stdin.readline

def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1 << word_dict[x])
    return answer

# a, n, t, i, c는 무조건 포함해야 함. 
N, K = map(int, input().split())
word_dict = {'b': 0, 'd':1, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'j': 6, 'k': 7, 'l': 8, 'm': 9, 
             'o': 10, 'p': 11, 'q': 12, 'r': 13, 's': 14, 'u': 15, 'v': 16, 'w': 17, 'x': 18, 'y': 19, 'z': 20}
words = []
for _ in range(N):
    words.append(''.join(set(list(input().rstrip()[4:-4])).difference('a', 'n', 't', 'i', 'c')))

if K < 5:
    print(0)
else:
    bin_list = [word_to_bin(x) for x in words]
    power_of_2 = [2**i for i in range(21)]

    answer = 0
    for comb in combinations(power_of_2, K-5):
        cur = sum(comb)
        count = 0
        for bin_number in bin_list:
            if bin_number & cur == bin_number:
                count += 1
        answer = max(answer, count)

    print(answer)