from collections import deque


'''
[✕]
board에 움직인 횟수 업데이트하면서 진행, 
현재 움직인 횟수가 board 깂보다 작으면 업데이트

ladder, snake는 리스트보단 딕셔너리가 낫긴 하겠다. ladder.values(), snake.keys() 이런식으로 접근하는게 유용할듯

초기 : ladder.items() 오름차순 정렬 
ladder end-start 가 최대인 start로 가기 위해 주사위 탐색
    if current ~ start 범위 내 존재하는 ladder 있으면 사용
    for 6, .., 1
        snake.items() 아니면 next+=i break 
    다 snake(current == next) 면 next = max([snake[current+1], .. snake[current+6]])

---
[✓] 
알고리즘을 general 하게 구현해놓고, 연산 최적화를 고려하는게 개미지옥으로 빠지지 않을 수 있다.
저렇게 일어날 수 있는 모든 상황을 가정해서 모든 케이스를 만들어놓을 고민은 이 이후에 하자.

bfs 알고리즘이 최적 해를 찾기까지 동작하는 과정을 잘 생각해야할 듯
- 6, 5, 4, 3, 2, 1 칸 움직이는 다음 depth 노드를 다 넣어주는데, 
- 이때 snake/ladder인 케이스를 따로 반영한 칸을 다음 노드로 넣어주면 간단한 문제였는데,
- 여기서 ladder인 경우에만 큐에 추가됐으면, snake인 경우는 배제됐으면,, 이런 specific한 경우를 복잡하게 생각하다보니
- 오히려 알고리즘의 정확성이 떨어지고, 문제를 구현하지 못했다.
'''

n, m = map(int, input().split()) # 사다리 개수, 뱀 개수

move = {}
for _ in range(n+m):
    k, v = map(int, input().split())
    move[k] = v
print(move)

queue = deque([(1, 0)])
visited = set([1])
while queue:
    print(queue)
    current, mv = queue.popleft()
    if current == 100:
        print(mv)
        break
    for i in range(6, 0, -1):
        next = current + i
        if next in move.keys(): next = move[next]
        if next <= 100 and next not in visited:
            queue.append((next, mv+1))
            visited.add(next)
            
