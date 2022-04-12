from heapq import heappush, heappop

def find(a, parents):
    if parents[a] == a:
        return parents[a]
    parents[a] = find(parents[a], parents)
    return parents[a]

def union(a, b, parents):
    a, b = find(a, parents), find(b, parents)
    if a == b:
        return 0 
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    heap = []
    parents = [i for i in range(n)]
    # cost, src, dst
    for a, b, c in costs:
        heappush(heap, (c, a, b))
    
    result = []
    while heap:
        if len(result) == n-1:
            break
        cost, src, dst = heappop(heap)
        if find(src, parents) != find(dst, parents):
            union(src, dst, parents)
            result.append(cost)
    return sum(result)