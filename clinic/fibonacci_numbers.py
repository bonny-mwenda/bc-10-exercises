'''Function to get a list of fibonacci numbers'''


def fibonacci(n):
    '''Get fibonacci numbers of the 1st n terms'''

    # Check that the input is valid
    if type(n) is not int:
        raise TypeError("Value must be integer")
    elif n == 0:
        return []
    elif n < 0:
        raise ValueError("Value must be greater than zero")

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

