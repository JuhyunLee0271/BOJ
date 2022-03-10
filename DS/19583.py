import sys
input = sys.stdin.readline

S, E, Q = input().split()

start = set()
end = set()

while True:
    try:
        time, name = input().split()
        if time <= S:
            start.add(name)
        if E <= time <= Q:
            end.add(name)
    except:
        break

print(len(start.intersection(end)))