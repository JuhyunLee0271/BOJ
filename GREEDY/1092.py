import sys
input = sys.stdin.readline

N = int(input())
crains = sorted(list(map(int, input().split())), key=lambda x:-x)

M = int(input())
boxes = sorted(list(map(int, input().split())), key=lambda x:-x)

if boxes[0] > crains[0]:
    print(-1)
    
else:
    result = 0
    while boxes:
        if not boxes:
            break
        for crane in crains:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        result += 1   
    print(result)