import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1 
        else:
            end = mid - 1
    return False


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    M = int(input())
    target = list(map(int, input().split()))

    for e in target:
        if binary_search(arr, e, 0, len(arr)-1): print(1)
        else: print(0)



