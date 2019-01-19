def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    maximum = 10000
    even_fibonacci = []
    for n in range(1, maximum):
        fib = fibonacci(n)
        if fib % 2 == 0:
            even_fibonacci.append(str(fib))
        if fib > maximum:
            break
    return ', '.join(even_fibonacci)


if __name__ == '__main__':
    print(main())
