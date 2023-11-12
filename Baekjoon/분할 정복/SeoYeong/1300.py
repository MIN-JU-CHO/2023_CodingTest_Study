def count_less_or_equal(mid, N):
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)
    return count

def find_kth_number(N, k):
    left, right = 1, N * N
    while left <= right:
        mid = (left + right) // 2
        if count_less_or_equal(mid, N) < k:
            left = mid + 1
        else:
            right = mid - 1
    return left

N = int(input())
k = int(input())