# 문제 풀이 링크: https://velog.io/@cuppizza/백준-10816-숫자-카드-2-파이썬-C
# 실행 시간: 860ms 메모리: 118520KB
import sys
input = sys.stdin.readline

N = int(input())
numCards = list(map(int, input().split()))
M = int(input())
inputNums = list(map(int, input().split()))

cardsCount = {}

for card in numCards:
    if card in cardsCount:
        cardsCount[card] += 1
    else:
        cardsCount[card] = 1

for num in inputNums:
    if num in cardsCount:
        print(cardsCount[num], end = " ")
    else:
        print(0, end = " ")

# 시간 초과 풀이
import sys
input = sys.stdin.readline

N = int(input())
numCards = list(map(int, input().split()))
M = int(input())
inputNums = list(map(int, input().split()))

numCards.sort()
counts = [0] * M

def bin_search(left, right, key, index):
    if left == right:
        if numCards[left] == key:
            counts[index]+=1
        return
    elif left > right:
        return
    else:
        mid = (left + right) // 2
        if numCards[mid] == key:
            counts[index]+=1
            bin_search(left, mid-1, key, index)
            bin_search(mid+1, right, key, index)
        elif numCards[mid] < key:
            bin_search(mid+1, right, key, index)
        else:
            bin_search(left, mid-1, key, index)

for i in range(M):
    bin_search(0, N-1, inputNums[i], i)
for count in counts:
    print(count, end = " ")
