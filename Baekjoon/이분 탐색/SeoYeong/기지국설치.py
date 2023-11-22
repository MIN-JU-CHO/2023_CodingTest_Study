
import math
# 각 s에서 +=w 를 한 값들을 리스트로 몰어넣고 

def solution(n, stations, w):
    answer = 0
    start = []
    end = []
    # 양 끝단에서 station-w가 1, n 넘어가는 애들 짤라주기
    for s in stations:
        start.append(s-w)
        end.append(s+w)
    print(start, end)
    for i, j in zip(start[1:], end[:-1]):
        print(i, j)
        if i-1 >= j+1:
            answer += math.ceil((i-1-(j+1)+1)/(w*2+1))
            print(answer)
    # 양 끝단 확인
    if start[0]-1 > 1:
        answer += math.ceil(start[0]-1/(w*2+1)); print(answer)
    if end[-1]+1 < n:
        answer += math.ceil((n - end[-1]+1 + 1)/(w*2+1)); print(answer)

def solution_1(n, stations, w): 
    idx = 1
    for i, s in enumerate(stations):
        if i == len(stations)-1:
            answer += math.ceil((n-idx)/(w*2+1))
            pass
        # idx ~ s-w 를 (w*2+1)로 나누고 ceil, idx = s+w
        answer += math.ceil((s-w-idx)/(w*2+1))
        idx = s+w+1
        
    return answer

solution(11, [4, 11], 1)
solution(16, [9], 2)
solution(13, [3, 7, 11], 1) #4
solution(5, [3], 2,)# 0
solution(6, [3], 2,) #1
solution(16, [1, 16], 2)# 2
solution(6, [4], 2) # 1
solution(11, [1, 4], 1) #2
solution(11, [1, 5], 1) #3
solution(5, [1, 2, 3, 4, 5], 1) # 0
solution(200000000, [100000000], 5) # 18181818