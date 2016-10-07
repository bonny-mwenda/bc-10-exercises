'''Fibonacci numbers of the 1st n terms'''


def fibonacci(n):
    # Initialize first two fibonacci numbers
    fib1 = 0
    fib2 = 1
    lst = []
    for i in range(n):
        lst.append(fib1)
        nextNum = fib1 + fib2
        fib2 = fib1
        fib1 = nextNum
    return(lst)
