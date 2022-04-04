import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
else:
    diff = []
    for i in range(len(sensor)-1):
        diff.append(sensor[i+1] - sensor[i])
    diff.sort(key=lambda x:-x)
    result = sum(diff)
    for i in range(K-1):
        result -= diff[i]
    print(result)
    