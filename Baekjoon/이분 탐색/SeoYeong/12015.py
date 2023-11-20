
import math
def its_not_sequential(lst):
    """
    deprecated
    """
    return len(list(filter(lambda x: x<0, [j-i for i, j in zip(lst[0:-1], lst[1:])])))


def dp(N: int, sequence: list) -> None:
    """timeout"""
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))


def bs(target: int, lst: list) -> int:
    l, r = 0, len(lst)-1
    while l <= r:
        mid = (l+r)//2
        print(l, r, lst[mid], target)
        if lst[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l if l < len(lst) else -1
    

def bs_main(sequence: list) -> None:
    lis = [math.inf]
    for num in sequence:
        if num > lis[-1]:
            lis.append(num); print(lis)
        else:
            idx = bs(num, lis)
            if idx != -1:
                lis[idx] = num; print(lis)
    print(len(lis))



# N = int(input())
# sequence = list(map(int, input().split()))

sequence = [10, 20, 10, 30, 20, 50]
# sequence = [10, 32, 20, 21, 22, 23, 24, 31]
# sequence = [4, 3, 2, 1, 3, 4, 5]
# sequence = [1, 2, 3, 4, 5,6]
bs_main(sequence)

