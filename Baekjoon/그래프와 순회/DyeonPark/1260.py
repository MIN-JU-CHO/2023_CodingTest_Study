import sys
from collections import defaultdict, deque

def input():
  return sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())

# 인접 리스트를 활용한 그래프 저장 
G = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# DFS - stack 자료구조 이용 (함수 호출 시 자동으로 활용 가능)
def dfs(V, G, visited):
    visited[V] = True
    print(V, end=" ")
    for i in sorted(G[V]):
        if not visited[i]:
            dfs(i, G, visited)

# BFS - queue 자료구조 이용 (deque를 이용해 생성)
def bfs(V, G):
  queue = deque([V])
  visited = [False] * (N + 1)
  visited[V] = True
  
  while queue:
    front = queue.popleft()
    print(front, end=' ')
    for i in sorted(G[front]):
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(V, G, [False] * (N + 1))
print()
bfs(V, G)
