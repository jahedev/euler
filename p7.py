"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# find smallest factor of any number, returns -1 if not found.
def smallest_factor(n):
    # try dividing 'n' starting from the number 2 upto half the size of 'n',
    # if the number is divisible with no remainder, then return that as the smallest factor of 'n'.
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return i
    return -1

# find all the factors of a number
def get_factors(n):
    last_factor = smallest_factor(n) # last successful factor
    current_factor = last_factor #  current factor will end the loop, when it equals -1
    factors = [] # where all the factors will be stored
    last_divided_number=n # to keep track of the found factors 'n' is divided by

    # smallest_factor(n) will return -1, when there is no smallest factor on 'n'
    while current_factor != -1:
        last_factor = current_factor # save the last successful factor in last_factor 
        factors.append(last_factor)
        
        last_divided_number /= last_factor
        
        current_factor = smallest_factor(last_divided_number)
    
    # multiply every factor, and divide that in 'n' to get the largest factor
    factors_multiplied=1
    for factor in factors:
        factors_multiplied *= factor
    largest_factor = int(n / factors_multiplied)
    factors.append(largest_factor)

    return factors

def get_prime(n):
    if n < 2:
        return -1

    current_prime = -1
    count = 2

    primes_found = 0

    while primes_found < n:
        if len(get_factors(count)) == 1:
            current_prime = get_factors(count)[0]
            primes_found += 1
        if primes_found == n:
            return current_prime
        count += 1


print(get_prime(10001))