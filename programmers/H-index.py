def calc(arr, mid):
    cnt = 0
    for num in arr:
        if num >= mid:
            cnt += 1
    return cnt

def solution(citations):
    citations.sort()
    start, end = 0 , citations[-1]
    
    while start <= end:
        mid = (start + end) // 2
        res = calc(citations, mid)
        if res < mid:
            end = mid - 1
        else:
            start = mid + 1
    return end