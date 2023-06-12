def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return round(a / b, 2)

# 모듈 테스트
if __name__ == '__main__':
    print(add(3, 5))
    print(subtract(10, 7))
    print(multiply(10, 7))
    print(divide(10, 7))