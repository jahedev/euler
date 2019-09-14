import math

def pbar(string):
    print('\r %s \r' % string, end='\r')

def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while math.pow(i, 2) <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

primes_found = 0
num_of_primes_to_find = 20000
sum_of_primes = 0

count = 2

while primes_found < num_of_primes_to_find:
    if is_prime(count):
        primes_found += 1
        sum_of_primes += count

    progress = (primes_found / num_of_primes_to_find) * 100
    pbar('Working... %.2f' % progress)

    count += 1

print('sum of primes: ' + str(sum_of_primes))