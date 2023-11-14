n = int(input())
k = int(input())

def count(v):
  cnt = 0
  for i in range(1,n+1):
    cnt += min(v//i, n) # v보다 작거나 같은 수 계산하기
  return cnt

def bs(min_value, max_value):
  print(f"bs({min_value}, {max_value})")
  global k
  if min_value > max_value: # 
    return min_value

  mid = (min_value + max_value) // 2  
  cnt = count(mid)                    
  print(mid, cnt)
  if cnt >= k:    # V보다 작거나 같은 수가 7개보다 크면 ⇒ V를 줄이기 
    return bs(min_value, mid-1)
  else:           # V보다 작거나 같은 수가 7개보다 작으면 ⇒ V를 키우기
    return bs(mid+1, max_value)                            

print(bs(1, k)) # v => 1 ~ k 확인하기


'''
1. bs(1, 7)
mid = 4
cnt = 6 => 7보다 작음, mid 키우기

2. bs(5, 7)
mid = 6
cnt = 8 => 7보다 큼, mid 줄이기

3. bs(5, 5)
mid = 5
cnt = 6 => 7보다 작음, mid 키우기

4. bs(6, 5)
return 6
'''
