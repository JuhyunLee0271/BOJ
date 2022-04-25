import sys
input = sys.stdin.readline

# N: 끊어진 기타줄의 수, M: 기타줄 브랜드의 수 
# [6개가 들어있는 패키지 가격, 낱개의 가격]
N, M = map(int, input().split())
package = each = sys.maxsize
for _ in range(M):
    a, b = map(int, input().split())
    package, each = min(a, package), min(b, each)

if package > each * 6:
    answer = N *  each
elif (N % 6) * each > package:
    answer = (N // 6) * package + package
else:
    answer = (N // 6) * package + (N % 6) * each
print(answer)