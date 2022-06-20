import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def backtracking(tmp_string: str, idx, plus, minus, mul, div):
    global max_answer, min_answer
    if idx == N:
        result = eval(tmp_string)
        min_answer = min(min_answer, result)
        max_answer = max(max_answer, result)
        return
        
    if plus > 0:
        backtracking(tmp_string + '+' + str(numbers[idx]), idx + 1, plus - 1, minus, mul, div)
    
    if minus > 0:
        backtracking(tmp_string + '-' + str(numbers[idx]), idx + 1, plus, minus - 1 , mul, div)
    
    if mul > 0:
        backtracking(tmp_string + '*' + str(numbers[idx]), idx + 1, plus, minus, mul - 1 , div)
    
    if div > 0:
        backtracking(tmp_string + '//' + str(numbers[idx]), idx + 1, plus, minus, mul, div - 1)
    
    return
    

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
min_answer, max_answer = 10**9, -10**9

backtracking(str(numbers[0]), 1, plus, minus, mul, div)

print(max_answer)
print(min_answer)