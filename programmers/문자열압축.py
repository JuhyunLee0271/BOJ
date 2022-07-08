def solution(s):
    answer = 10e9
    if len(s) == 1:
        return 1
    for k in range(1, len(s)):
        current, result = "", ""
        word_dict = dict()
        for i in range(0, len(s), k):
            if not current:
                current = s[i:i+k]
                word_dict[current] = 1
            elif current == s[i:i+k]:
                word_dict[current] += 1
            elif current != s[i:i+k]:
                key, value = current, word_dict[current]
                if value == 1: result += str(key)
                else: result += str(value) + str(key)
                current = s[i:i+k]
                word_dict[current] = 1
        key, value = current, word_dict[current]
        if value == 1: result += str(key)
        else: result += str(value) + str(key)
        answer = min(answer, len(result))
    return answer