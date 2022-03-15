import heapq
import sys
input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
heapq.heapify(cards)

result = 0
while len(cards) > 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    result += num1 + num2
    heapq.heappush(cards, num1+num2)

print(result)



    
