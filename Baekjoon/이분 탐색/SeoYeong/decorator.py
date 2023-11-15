'''
Decorator
- method, class 의 동작을 변경하거나 확장하는데에 사용됨
- 기존 코드를 수정하지 않고 추가적인 기능을 적용할 수 있다
- 구조
    - decorator 함수 : 데코레이터의 주체, 다른 함수를 인자로 받고 이 함수 내에서 다른 함수(usually wrapper) 정의, 반환
    - wrapper 함수 : 데코레이터가 적용될 원래 함수를 감싸는 역할. 원래 함수가 호출되기 전, 후에 추가적인 로직을 실행할 수 있게 한다.
    - 함수 : 데코레이터가 적용될 실제 함수
- 작동 원리
    - 함수 정의 위에 @
    - 해당 함수 호출 시 데코레이터에 의해 반환된 wrapper 함수가 실제로 호출됨
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
'''
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
'''

print()


'''
예시 1. 데이터 캐싱
- 데이터, 결과 등을 임시로 저장
- 계산 비용 높은 작업 반복적으로 수행해야 할 때 캐싱 사용하면 성능 향상 가능
'''

import time
def cache(func):
    cached_values = {}  # 캐시를 저장할 딕셔너리
    def wrapper(n):
        if n not in cached_values:  # 캐시에 없다면 계산하고 저장
            cached_values[n] = func(n)
        return cached_values[n]  # 캐시된 값을 반환
    return wrapper

@cache
def cached_fibonacci(n):
    if n < 2:
        return n
    return cached_fibonacci(n-1) + cached_fibonacci(n-2)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(fibonacci(10)) 
end = time.time()
print(f"캐싱 안했을 때 : {end-start}")

start = time.time()
print(cached_fibonacci(10)) 
end = time.time()
print(f"캐싱했을 때 : {end-start}")


'''
예시 2. 지연 로딩
- 데이터가 크거나 로드하는데 시간이 오래 걸리는 경우
- 데이터가 실제로 필요할 때까지 로딩을 연기
- 리소스를 절약하고 애플리케이션의 시작 시간을 단축하는데 유용
'''
def lazy_load(func):
    result = None
    def wrapper(*args, **kwargs):
        nonlocal result
        if result is None:  # 데이터가 로드되지 않았다면 로드
            result = func(*args, **kwargs)
        return result  # 로드된 데이터 반환
    return wrapper

@lazy_load
def load_large_data():
    print("Loading large data...")
    return "Large Data Loaded"

start = time.time()
print(load_large_data())  # 첫 호출 시 로드
end = time.time()
print(f"지연 전 : {end-start}")

start = time.time()
print(load_large_data())  # 이미 로드되어 있으므로 바로 반환
end = time.time()
print(f"지연시켰을 때 : {end-start}")
