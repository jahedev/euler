import time # to measure time taken

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

# find the largest prime number of a number
# if you feed it a prime number, like 17, it will just feed it back to you.
def largest_prime_number(n):
    factors = get_factors(n) # first get all the factors

    # starting from the largest factor, check if it is prime
    # if not, then continue to the next largest factor.
    for i in range(len(factors)-1, -1, -1):
        if smallest_factor(factors[i]) == -1:
            return factors[i]
        return -1


num = 600851475143 # the number we will test

start = time.process_time() # to measure time taken
lpn = largest_prime_number(num)
time_taken = ((time.process_time() - start)*1000)

# print(get_factors(num))
print("Largest Prime Number:", lpn)

print('That took: ',"%.3f" % time_taken, 'miliseconds')
