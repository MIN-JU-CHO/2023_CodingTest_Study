v, e = map(int, input().split())
inf = 11*(v-1)+1 # w 최댓값 10, 경로가 모든 노드를 거쳐서 오는 최대 경로 케이스를 고려하면 최댓값은 11*(v-1)
start = int(input())
# graph = [[inf for _ in range(v)] for _ in range(v+1)]
graph = [[-1 for _ in range(v+1)] for _ in range(v+1)]
for _ in range(v):
    u, v, w = map(int, input().split())
    graph[v][u] = w

'''
end 정점을 하나씩 설정해서 graph[start]에 업데이트해나가기
end 정점으로 들어오는 정점을 거꾸로 타고 가면서 시작 정점으로 갈 수 있는지 체크 
    -> 갈 수 있고, 해당 경로의 가중치가 graph[start][end] 보다 작으면 해당 값으로 업데이트

max graph 크기 ?
파이썬에서 int는 28바이트
20000*20000*28 (byte) = 10681 MB(약 10.7GB) 
가중치 최댓값이 10이니까 메모리초과 뜨면 numpy 라이브러리에서 np.int8 로 채워보자
- 역시나 메모리 초과..

행이 end vertices, 열이 start vertices, 안에 값이 가중치를 나타내도록 구현
graph[i] : 각 인덱스는 i로 들어오는 정점과 그의 가중치
    - i 로 들어오는 애들(j) 확인 -> min(start to j + j to i)
    - 최종 값을 graph[start][i]에 저장
'''
start_to_idx = [0 for _ in range(v+2)]

print(graph)
for i in range(1, v+1):
    if i == start: continue
    optimal_path = inf
    for j in range(1, v+1):
        if i == j or graph[i][j] == -1: continue
        optimal_path = min(optimal_path, graph[i][j] + start_to_idx[j])
    start_to_idx[i] = optimal_path


for i in range(1, v+2):
    if i != start and start_to_idx[i] == 0: print('INF')
    else: print(start_to_idx[i])
