def make_arr(numbers, n):
    arr = []
    for num in numbers:
        _num = str(bin(num)[2:])
        _num = (n-len(_num))*"0"+_num
        arr.append(list(map(int, _num)))
    return arr

def solution(n, arr1, arr2):
    arr1, arr2 = make_arr(arr1, n), make_arr(arr2, n)
    answer = []
    for i in range(n):
        temp = ""
        for j in range(n):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer