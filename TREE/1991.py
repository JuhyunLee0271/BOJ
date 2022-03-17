import sys
input = sys.stdin.readline
s = [[0,0,0] for i in range(26)]

N = int(input())
for _ in range(N):
    node, left, right = map(str, input().rstrip().split())
    item = ord(node) - 65
    s[item][0], s[item][1], s[item][2] = node, left, right

def preorder(start):
    print(start, end="")
    if s[ord(start)-65][1] != ".":
        preorder(s[ord(start)-65][1])
    if s[ord(start)-65][2] != ".":
        preorder(s[ord(start)-65][2])

def midorder(start):
    if s[ord(start)-65][1] != ".":
        midorder(s[ord(start)-65][1])
    print(start, end="")
    if s[ord(start)-65][2] != ".":
        midorder(s[ord(start)-65][2])

def postorder(start):
    if s[ord(start)-65][1] != ".":
        postorder(s[ord(start)-65][1])
    if s[ord(start)-65][2] != ".":
        postorder(s[ord(start)-65][2])
    print(start, end="")

preorder("A")
print()
midorder("A")
print()
postorder("A")  
print()