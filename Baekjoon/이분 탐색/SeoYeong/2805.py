
def bs(trees: list, M: int):
    l, r = 1, max(trees)
    while l <= r:
        mid = (l + r) // 2
        blocks = sum(x-mid for x in trees if x>=mid)
        if blocks >= M:
            l = mid + 1
        else:
            r = mid - 1
    print(r)
# N, M = map(int, input().split()) # 나무 수, 필요한 나무 길이
# trees = [int(input()) for _ in range(N)] # 나무 길이들

# N, M, trees = 4, 7, [20, 15, 10, 17] # 15
# N, M, trees = 5, 20, [4, 42, 40, 26, 46] # 36
# 반례
# N, M, trees = 2, 10, [3, 9] # 1
# N, M ,trees = 4, 8, [20, 15, 10, 17] #14
# N, M, trees = 2,11,[10,10] #4
# N, M, trees = 3, 1, [1, 2, 2] #1
# N, M, trees = 4, 10, [1, 4, 5, 7] #2
# N, M, trees = 5, 2000000000, [900000000, 900000000, 900000000, 900000000, 900000000]#500000000
# N, M, trees = 1, 1000000000, [1000000000] #0
# N, M, trees = 1, 1, [1000000000] #999999999
# N, M, trees = 6, 12, [19, 9, 18, 20, 17, 8] #15
N, M, trees = 5, 14, [4, 22, 10, 16, 36] #22

bs(trees, M)
