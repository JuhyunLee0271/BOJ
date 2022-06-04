import sys
input = sys.stdin.readline

N = int(input())
loss = list(map(int, input().split()))
joy = list(map(int, input().split()))
arr = [(0, 0)] + list(zip(loss, joy))
knapsack = [[0 for _ in range(100)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 100):
        loss, joy = arr[i][0], arr[i][1]
        if j < loss:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j-loss] + joy, knapsack[i-1][j])

print(knapsack[-1][-1])


    