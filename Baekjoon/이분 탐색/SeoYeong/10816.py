from collections import Counter


_ = int(input()) # N 필요없음
cards = Counter(map(int, input().split()))
_ = int(input())
num = list(map(int, input().split()))
print(cards, num)

for n in num:
    if n not in cards.keys():
        print(0, end=' ')
    else:
        print(cards[n], end=' ')
