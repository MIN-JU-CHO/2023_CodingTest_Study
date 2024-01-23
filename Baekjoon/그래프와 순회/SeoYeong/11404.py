import sys
input = sys.stdin.readline

def floyd():
    for i in range(n): # i 정점의
        for j in range(n): # j 정점으로의 최단거리 구할때
            if i == j : continue
            for k in range(n): # k 정점을 거쳐갈 때
                if i == k : continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                graph[i][k] = min(graph[i][k], graph[i][j]+graph[j][k])
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])


n = int(input())
m = int(input())
inf = 1e10
graph = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n): graph[i][i] = 0

"""
i도시에서 j 도시로 가는 방법 여러가지 일떄 최소 경로만 남기는 방법?
1. 일단 다 저장하고 counter같은 거 쓴다.
    - counter ) subclass of dict, so 
2. 저장할 때 최솟값 계속 업데이트한다.
-> 둘 다 X, 어차피 n*n 배열에다가 i->j의 최소 거리 업데이트 할거니까 지금도 똑같이 최소값 업데이트하면 됨
"""
for _ in range(m):
    start_city, end_city, fee = map(int, input().split())
    graph[start_city-1][end_city-1] = min(graph[start_city-1][end_city-1], fee)
    
floyd()

for i in range(n):
    print(' '.join(str(graph[i][j]) if graph[i][j] != inf else '0' for j in range(n)))

        