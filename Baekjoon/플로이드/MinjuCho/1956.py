# pypy 제출 실행 시간: 936ms 메모리: 112352KB
import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().strip().split())
adj = [[INF for _ in range(v+1)] for __ in range(v+1)]
while e:
    e-=1
    a, b, c = map(int, input().strip().split())
    if c < adj[a][b]:
        adj[a][b] = c
for i in range(v+1):
    for s in range(v+1):
        for t in range(v+1):
            if adj[s][i] + adj[i][t] < adj[s][t]:
                adj[s][t] = adj[s][i] + adj[i][t]
shortest = INF
for s in range(v+1):
    for t in range(v+1):
        if adj[s][t]!=INF and adj[t][s]!=INF and adj[t][s]+adj[s][t] < shortest:
            shortest = adj[t][s] + adj[s][t]
if shortest == INF:
    print(-1)
else:
    print(shortest)
