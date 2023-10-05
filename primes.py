"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    prime = []
    start = 2
    if number_of_primes>0:
        while len(prime) < number_of_primes:
            primeTest = []
            for i in prime:
                print(i)
                if start%i==0:
                    print("pass")
                    primeTest.append(start)
            if primeTest:
                prime += []
            else:
                prime += [start]
            start += 1
        return prime
    else:
        raise ValueError("Enter a valid value")

print(primes(0))
