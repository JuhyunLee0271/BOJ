temp = []
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    temp.append(i)
result = [i for i in range(1, 10000) if i not in temp]
for e in result:
    print(e)