"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    start = 2
    while (list.length()!=number_of_primes):
        for value in range(2,int(start**0.5)+1):
            if (start % value != 0):
                list.append(start)
        start+=1
    return list
