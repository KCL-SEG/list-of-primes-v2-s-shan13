"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Input must be greater than 0")
    list = []
    i = 2
    while len(list) < number_of_primes:
        add = True
        for j in range(2,i):
            if i%j == 0:
                add = False
                break
        if add:
            list.append(i)
        i += 1
    return list

print(primes(1))