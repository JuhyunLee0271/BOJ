from itertools import permutations
import re

def solution(expression):
    answer = 0
    numbers, operators = [], []
    
    for e in re.findall('[+-/*/]|\d+', expression):
        if e in ['*', '+', '-']: 
            operators.append(e)
        else: 
            numbers.append(int(e))

    for prio in list(permutations(['*','+','-'], 3)):
        _numbers = numbers[:]
        _operators = operators[:]
        
        for oper in prio:
            while oper in _operators:
                idx = _operators.index(oper)
                if oper == '+':
                    temp = _numbers[idx] + _numbers[idx+1]
                if oper == '-':
                    temp = _numbers[idx] - _numbers[idx+1]
                if oper == '*':
                    temp = _numbers[idx] * _numbers[idx+1]
                del _numbers[idx]
                del _numbers[idx]
                del _operators[idx]
                _numbers.insert(idx, temp)
        answer = max(answer, abs(_numbers[0]))
    return answer