'''A function that gets a list of prime numbers'''


def get_primes(n):
    '''Get a list of first n prime numbers'''

    # Create a list with the first prime number
    lst = [2]
    # Test each number for primeness, starting with 3
    testNum = 3

    while True:
        prime = True
        # Check if number under test is prime
        for item in lst:
            if testNum % item == 0:
                prime = False
                break
                testNum += 1
        if prime:
            lst.append(testNum)
        testNum += 1

        # Break if len(lst) == n
        if len(lst) == n:
            break
    return lst
