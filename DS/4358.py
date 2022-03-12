import sys
input = sys.stdin.readline
trees = dict()
cnt = 0
while True:
    try:
        tree = input().rstrip()
        if not trees.get(tree):
            trees[tree] = 1
        else:
            trees[tree] += 1
        cnt += 1
    except:
        break

result = []
print(cnt)
for tree, count in trees.items():
    result.append((tree, round(float(count)/cnt*100,4)))

for tree, rate in sorted(result, key=lambda x:x[0]):
    print(tree, rate)