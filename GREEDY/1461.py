import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

neg = sorted([num for num in arr if num < 0])
pos = sorted([num for num in arr if num > 0], reverse=True)

temp = []

for i in range(0, len(neg), M):
    temp.append(-neg[i])

for i in range(0, len(pos), M):
    temp.append(pos[i])

temp.sort()
print(2*sum(temp[:-1]) + temp[-1])