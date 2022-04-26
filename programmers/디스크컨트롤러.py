from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    heap = []
    last, now = -1, 0
    i = 0
    
    while i < len(jobs):
        for job in jobs:
            if last < job[0] <= now:
                heappush(heap, (job[1], job[0]))
        if heap:
            cost, req = heappop(heap)
            last = now
            now += cost
            answer += (now - req)
            i += 1
        else:
            now += 1
    answer //= len(jobs)
    return answer
