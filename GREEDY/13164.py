import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))

diff = sorted([arr[i+1] - arr[i] for i in range(N-1)])
print(sum(diff[:N-K]))