from collections import Counter, deque

def is_in_range(x: int, y: int) -> bool:
    global n
    if x >=0 and x<n and y>=0 and y<n:
        return True
    return False


def search_apartment(graph: list, x: int, y: int, idx : int) -> list:
    q = deque([(x, y)])
    rotate = [[-1, 0, 1, 0],
              [0, 1, 0, -1]] # 시계방향
    while q:
        nx, ny = q.popleft()
        # 4방향 탐색
        for i in range(4):
            sx, sy = nx + rotate[0][i], ny + rotate[1][i]
            if is_in_range(sx, sy) and graph[sx][sy]==1:
                graph[sx][sy] += idx
                q.append((sx, sy))
    return graph
            

n = int(input())
graph = []
for _ in range(n): graph.append([int(i) for i in input()])

# n = 7
# graph = [[0, 1, 1, 0, 1, 0, 0], 
#          [0, 1, 1, 0, 1, 0, 1], 
#          [1, 1, 1, 0, 1, 0, 1], 
#          [0, 0, 0, 0, 1, 1, 1], 
#          [0, 1, 0, 0, 0, 0, 0], 
#          [0, 1, 1, 1, 1, 1, 0], 
#          [0, 1, 1, 1, 0, 0, 0]]


"""
graph 전부 다 하나의 단지 
    0 -> 1 \n n*n 출력  ..(1)
    x -> search, result에 0 무조건 있을 수 밖에 없음  
         혼자 똑 떨어져있는 단지 (아파트 한 개로 이루어져있는, result key 값 1)
                o  -> result[1]+len(result.keys())-2) \n 
                                result[1]번 1 출력 \n 던지 아파트 개수 오름차순 출력  ..(2)
                x  -> len(result.keys())-1 \n 단지 아파트 개수 오름차순 출력        ..(3)
"""

# (1)
if sum(sum(graph, [])) == n*n:
    print(f"1\n{n*n}")
else:
    idx = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                graph = search_apartment(graph, i, j, idx)
                idx += 1


    result = dict(Counter(sum(graph, [])))
    result.pop(0)
    
    # (2)
    if 1 in result.keys():
        numof_alone_park = result[1]
        print(numof_alone_park + len(result.keys())-1)
        for i in range(numof_alone_park):
            print(1)
        result.pop(1)
    # (3)
    else:
        print(len(result.keys())) # 단지 개수

    result = dict(sorted(result.items(), key=lambda item: item[1]))
    for v in result.values():
        print(v)