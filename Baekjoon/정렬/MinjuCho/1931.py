import sys
input = sys.stdin.readline
n = int(input().strip())
demand = []
for i in range(n):
  demand.append(list(map(int, input().strip().split())))
  
demand.sort(key=lambda x:(x[1], x[0]))
result = [demand[0]]

for i in range(1, n):
  if result[-1][1] <= demand[i][1] \
  and result[-1][1] <= demand[i][0]:
    result.append(demand[i])
print(len(result))