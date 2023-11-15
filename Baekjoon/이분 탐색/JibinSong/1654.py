def count(mid):  # 랜선 개수 세기
  global arr
  c = 0
  for i in arr:
    c += i // mid
  return c


def bs(min_length, max_length):
  global length
  if min_length > max_length:
    return
  mid = (min_length + max_length) // 2
  print(min_length, mid, max_length)
  cnt = count(mid)
  print(cnt)
  if cnt >= k:  # k개보다 크면 길이 늘리기
    length = mid
    return bs(mid + 1, max_length)  # => 길이 늘리기
  else: #  => 길이 줄이기
    return bs(min_length, mid - 1)

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# print(arr)

length = 0
max_length = sum(arr) // k
min_length = max(max(arr) // k, 1) # ZeroDivisionError 해결
print(min_length, max_length) # 0, 1
bs(min_length, max_length)
print(length)
