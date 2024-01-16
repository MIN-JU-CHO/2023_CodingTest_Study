""" 문제
n개의 마을 
- 각 마을에 한 명의 학생이 삼
- 마을 사이 m개의 단방향 도로 있음
    - 오고가는 길 다를 수 있음
- i번째 길을 지나는데 Ti 시간 소요

n명의 학생이 마을 x에 모여서 파티
- 해당 마을로 갔다가 다시 자기 마을로 돌아가려고 할때 전체 최단시간
- 4, 8, 2 -> 정점 4개, 간선 8개, 2번정점에서 집합"""

"""풀이
- 다른 모든 정점으로부터 x까지의 최단거리를 반대롤 생각해보면
- 시작 정점으로부터 모든 정점까지의 최단거리를 구하는 다익스트라를 생각하면 된다.
- 문제는 도로가 단방향이니 왕복 길이 동일 시간임이 보장되지 않는다는 점이다.
    x로부터 다른 모든 정점까지의 최단거리를 구하는 것 뿐만 아니라, 모든 정점에서 x까자의 최단거리또한 구해야한다.
"""
import heapq

# find optimal path of from start to vi (start < vi)
def dijkstra(g: list):
    distance = [inf for _ in range(n+1)]
    distance[x] = 0 # start로부터 각 정점까지의 최단거리 저장 -> start-start 거리 0으로 초기화
    hq = []
    heapq.heappush(hq, (0, x))
    while hq:
        cw, cv = heapq.heappop(hq) # 가장 가중치 작은 정점 pop
        if distance[cv] < cw: continue
        for nw, nv in g[cv]: # 가중치 작은 정점 기준으로 인접 정점 탐방, distance 배열에 저장된 값보다 가중치 더한 경로값 작으면 distance 업데이트
            w = nw+cw
            if distance[nv] > w:
                distance[nv] = w
                heapq.heappush(hq, (w, nv))
    return distance


inf = 1e10
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    reverse_graph[b].append((w, a))

d1 = dijkstra(graph)
d2 = dijkstra(reverse_graph)
print(d1, d2, [x+y for x, y in zip(d1, d2)])
print(max([x+y for x, y in zip(d1, d2)][1:]))

