from collections import deque

def search_by_index(lettace_location: deque):
    print(lettace_location)
    
    insect = 0
    # visited = [lettace_location[0]]

    while lettace_location:
        # lettace_location 탐색 항상 다 해야되는가?
        # 아니면 정렬해서 안붙어있는거 나오면 pass해도되는가?
        ## 1. 일단 다 돌아보고 시간초과 나면 다시 수정해보자
        visited = [lettace_location[0]]
        for (nx, ny) in lettace_location:
            for (sx, sy) in visited:
                # print(lettace_location, visited)
                if (nx, ny) not in visited and (nx==sx and abs(ny-sy)==1) or (abs(nx-sx)==1 and ny==sy):
                    visited.append((nx, ny))
        print(f"visited : {visited}\nlettace_location : {lettace_location}")
        for (sx, sy) in visited:
            lettace_location.remove((sx, sy))
                
        insect += 1
    print(insect)
        
    


test_case = int(input())
for _ in range(test_case):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    lettace_location = deque([])
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
        lettace_location.append((x, y))

    search_by_index(lettace_location)
    