import sys
input = sys.stdin.readline


def recursive(op_list: list, length: int):
    if len(op_list) == length:
        operator_list.append(op_list.copy())
        return

    op_list.append(' ')
    recursive(op_list, length)
    op_list.pop()
    
    op_list.append('+')
    recursive(op_list, length)
    op_list.pop()
    
    op_list.append('-')
    recursive(op_list, length)
    op_list.pop()

for _ in range(int(input())):
    N = int(input())
    number_list = [i for i in range(1, N+1)]
    operator_list = []
    recursive([], N-1)

    for operators in operator_list:
        num_string = ""
        for i in range(N-1):
            num_string += str(number_list[i]) + operators[i]
        num_string += str(number_list[-1])
        if eval(num_string.replace(' ','')) == 0:
            print(num_string)
    print()
            
