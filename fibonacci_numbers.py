'''Function to get a list of fibonacci numbers'''


def fibonacci(n):
    '''Get fibonacci numbers of the 1st n terms'''

    # Initialize first two fibonacci numbers
    fib1 = 0
    fib2 = 1
    lst = []
    # Add the last number and second last number
    for i in range(n):
        lst.append(fib1)
        nextNum = fib1 + fib2
        fib2 = fib1
        fib1 = nextNum
    return(lst)
