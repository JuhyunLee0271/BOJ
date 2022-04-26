def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))  
    dic = {gems[0]:1,}
    s,e = 0,0 
    while s<N and e<N:
        if len(dic) < kind:  
            e += 1
            if e == N:
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1
            
        else: 
            if (e-s+1) < (answer[1]-answer[0]+1):
                answer = [s,e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1

    answer[0] += 1
    answer[1] += 1
    return answer