
def bs(array: list, target: int):
    l, r = array[0], array[-1]
    while l <= r:
        mid = (l+r)//2
        mid_val = array[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            l = array[mid+1]
        else:
            r = array[mid-1]
    return -1


# N,C = map(int, input().split())
# house = []
# for _ in range(N):
#     house.append(int(input()))
# house.sort()
N, C, house = 5, 3, [1, 2, 4, 8, 9]
distance = []
for i in range(N):
    for j in house[i+1:]:
        distance.append(j-house[i])
distance = list(set(distance))

ans = bs(distance, C)
print(ans)
