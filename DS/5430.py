from collections import deque
T = int(input())
for _ in range(T):
    commands = list(input().replace('RR',''))
    length = int(input())
    queue = deque(input()[1:-1].split(','))

    if commands.count('D') > length:
        print("error")
        continue

    if not queue and commands.count('D') == 0:
        print("[]")
        continue

    reverse = False
    for command in commands:
        if command == 'R':
            if reverse == False: reverse = True
            else: reverse = False
        elif command == 'D':
            if reverse == False: queue.popleft()
            else: queue.pop()
    
    if reverse: result = list(reversed(queue))
    else: result = list(queue)
    
    print('['+','.join(result)+']')
    