from collections import Counter

def convert(str):
    temp = []
    str = str.lower()
    for i in range(len(str)-1):
        temp.append(str[i] + str[i+1])
    return [word for word in temp if word.isalpha()]

def solution(str1, str2):
    answer = 0
    s1, s2 = convert(str1), convert(str2)
    if not s1 and not s2:
        answer = 1
    else:
        temp = dict()
        for key, value in Counter(s1).items():
            if key not in temp: temp[key] = [value]
            else: temp[key].append(value)
        for key, value in Counter(s2).items():
            if key not in temp: temp[key] = [value]
            else: temp[key].append(value)
        
        a, b = 0, 0
        for key, value_list in temp.items():
            min_val, max_val = min(value_list), max(value_list)
            b += max_val
            if len(value_list) > 1: a += min_val
        answer = a / b
        
    return int(answer*65536)