import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    answer = (V//P)*L + min(V%P, L)
    print(F"Case {i}: {answer}")
    i += 1
    