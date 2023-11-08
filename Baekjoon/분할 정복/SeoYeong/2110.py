# 메모리 초과
def deprecated(N, C, house):
    distance = []
    for i in range(N):
        for j in house[i+1:]:
            distance.append(j-house[i])
    distance = list(set(distance))

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
    
    ans = bs(distance, C)
    print(ans)

def can_install_router(house: list, distance: int, C: int):
    cnt = 1 # 첫 번째 집에는 공유기 일단 무조건 설치
    last_installed = house[0]

    for i in range(1, len(house)):
        if house[i] - last_installed >= distance:
            cnt += 1
            last_installed = house[i]
    return cnt >= C

def find_max_distance(house: list, C: int):
    l, r = 1, house[-1]-house[0] # 설치 가능한 최소 거리, 최대 거리
    result = 0

    while l <= r:
        mid = (l+r) // 2
        if can_install_router(house, mid, C):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


N,C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
ans = find_max_distance(house, C)
print(ans)