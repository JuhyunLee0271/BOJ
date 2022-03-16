import sys
input = sys.stdin.readline

def compare(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]: count += 1
    return count

A, B = input().rstrip().split()
A = list(A)
B = list(B)

diff = len(B) - len(A)
pair = [[i, diff-i] for i in range(0, diff+1)]
result = 1000
for a, b in pair:
    B_copy = B.copy()
    for _ in range(a):
        del B_copy[0]
    for _ in range(b):
        del B_copy[-1]
    result = min(result, compare(A, B_copy))
print(result)
        
        



