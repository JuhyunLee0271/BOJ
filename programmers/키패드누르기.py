point = {
    '1': [0,0], '2': [0,1], '3': [0,2],
    '4': [1,0], '5': [1,1], '6': [1,2],
    '7': [2,0], '8': [2,1], '9': [2,2],
    '*': [3,0], '0': [3,1], '#': [3,2]
}

def dist(a, b):
    a, b = str(a), str(b)
    return abs(point[a][0] - point[b][0]) + abs(point[a][1] - point[b][1])

def solution(numbers, hand):
    answer = ''
    cur = ['*', '#']
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            cur[0] = num
        elif num in [3, 6, 9]:
            answer += "R"
            cur[1] = num
        else:
            L_dst, R_dst = dist(num, cur[0]), dist(num, cur[1])
            if L_dst < R_dst or (L_dst == R_dst and hand == "left"):
                answer += "L"
                cur[0] = num
            elif L_dst > R_dst or (L_dst == R_dst and hand == "right"):
                answer += "R"
                cur[1] = num
    return answer