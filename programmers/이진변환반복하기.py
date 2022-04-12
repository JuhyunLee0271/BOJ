def solution(s):
    answer = []
    while s != '1':
        answer.append(s.count('0'))
        s = s.replace('0','')
        s = bin(len(s))[2:]
        
    return [len(answer), sum(answer)]