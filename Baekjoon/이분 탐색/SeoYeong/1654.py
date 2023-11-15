
def bs(N, strings):
    l, r = 1, max(strings)
    while l <= r:
        mid = (l+r)//2
        cnt = sum(x//mid for x in strings)
        if N <= cnt:
            l = mid + 1
        else:
            r = mid - 1
    print(r)

# initial solution
class CuttingLan():
    def __init__(self, N: int, K: int, strings: list) -> None:
        self.N = N # 필요한 랜선 개수
        self.K = K # 현재 갖고있는 랜선 개수(len(strings))
        self.strings = strings


    def is_it_possible(self, length: int) -> bool:
        """
        나누는 기준이 되는 랜선 길이를 받아서 K개의 동일 길이 랜선 만들수있는지 검사
        K 이상이먼 True
        """
        return self.K <= sum(x//length for x in self.strings)


    def bs(self, l: int, r: int):
        """
        strings 최솟값, 최소길이 기준으로 이분탐색 - 해당 길이로 뒤에 랜선 잘라보면서 개수 만족하는지 검사
        """
        result = r
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if self.is_it_possible(mid):
                # K보다 큼(또는 같을수도) -> 더 크게크게 잘라야함
                result = mid
                l = mid+1
            else:
                r = mid-1
        print(result)
                  


# K, N = map(int, input().split())
# strings = [int(input()) for _ in range(K)]
# K, N, strings = 4, 11, [802, 743, 457, 539] # 200
# K, N, strings = 2, 3, [3, 2] #1
# K, N, strings = 1, 1, [21474828] #21474828
# K, N, strings = 5, 5, [1, 1, 1, 1, 1] # 1
# K, N, strings = 4, 4, [2, 1, 2, 1] # 1
# K, N, strings = 3, 6, [40, 20, 10] #10
# K, N, strings = 4, 4, [9, 9, 9, 10] #9

## 반례
# 길이 하나가 다른 길이값을 최장길이로 나눈 값보다 작은 케이스
# ans 500 but resulted 1
K, N, strings = 3, 3, [1000, 1000, 1]

# 탐색 0부터 시작할 경우 divbyzero 발생 가능
# K, N, strings = 1,1, [1]

# K개의 길이값과 최장 길이값이 모두 같은 경우
# K, N, strings = 5, 5, [2, 2, 2, 2, 2]

# K, N, strings = 1, 3, [3]


# lan = CuttingLan(N, K, strings)
# lan.bs(1, min(strings))

bs(N, strings)