import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
commands = list(map(int, input().split()))

oper = ['+', '-', '*', '/']
operand = []

for i in range(len(commands)):
    for j in range(commands[i]):
        operand.append(oper[i])

operands = list(set(permutations(operand)))
results = []

for i in range(len(operands)):
    temp = numbers[0]
    for j in range(1, len(numbers)):
        if operands[i][j-1] == '+':
            temp = (temp + numbers[j])
        elif operands[i][j-1] == '-':
            temp = (temp - numbers[j])
        elif operands[i][j-1] == '*':
            temp = (temp * numbers[j])
        elif operands[i][j-1] == '/':
            temp = (int(temp / numbers[j]))
    results.append(temp)

print(max(results))
print(min(results))