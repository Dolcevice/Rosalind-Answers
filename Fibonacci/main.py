def rabbit_fib(n, k, start):
    if n == 0:
        return 0
    if n == 1:
        return start
    else:
        return rabbit_fib(n - 1, k, start) + (k * rabbit_fib(n - 2, k, start))


print(rabbit_fib(5, 3, 1))
