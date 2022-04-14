import sys
input = sys.stdin.readline   

def DFS(index, result, plus, minus, mul, div):
    global min_answer, max_answer
    if index == N:
        min_answer = min(min_answer, result)
        max_answer = max(max_answer, result)
        return
    if plus > 0:
        DFS(index+1, result + numbers[index], plus - 1, minus, mul, div)
    if minus > 0:
        DFS(index+1, result - numbers[index], plus, minus - 1, mul, div)
    if mul > 0:
        DFS(index+1, result * numbers[index], plus, minus, mul - 1, div)
    if div > 0:
        DFS(index+1, int(result / numbers[index]), plus, minus, mul, div-1)
        

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_answer = sys.maxsize
max_answer = -sys.maxsize

DFS(1, numbers[0], plus, minus, mul, div)

print(max_answer)
print(min_answer)