
import math

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = fibonacci_recursive(n - 1)
    fib.append(fib[-1] + fib[-2])
    return fib

def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num


def fibonacci_spiral(n):
    fib = fibonacci(n)
    golden_angle = math.pi * (3 - math.sqrt(5))
    points = []
    for i, radius in enumerate(fib):
        theta = i * golden_angle
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        points.append((x, y))
    return points

def fibonacci_word(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "0"
    elif n == 2:
        return "01"
    
    word = ["0", "1"]
    for _ in range(2, n):
        word.append(word[-2] + word[-1])
    return "".join(word)
