PI = 3.141592653589793

def plus(a, b):
    return a+b

def devide(a, b):
    return a / b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def mod(a, b):
    return a % b


# 斐波那契(fibonacci numbers)数列模块

def fib(n):    # 打印斐波那契数列直到 n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    fib(int(sys.argv[2]))


def fib2(n):   # 返回斐波那契数列直到 n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


def sum_odd_numbers(number):
    total = 0
    for i in range(1, number + 1, 2):
        total += i
    return total





