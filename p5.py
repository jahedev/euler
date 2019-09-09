"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import Counter

min = 1
max = 20

### START HELPING FUNCTIONS ###

# find smallest factor of any number, returns -1 if not found.
def smallest_factor(n):
    # try dividing 'n' starting from the number 2 upto half the size of 'n',
    # if the number is divisible with no remainder, then return that as the smallest factor of 'n'.
    for i in range(2, int(n/2)):
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

### END HELPING FUNCTIONS ###

def smallest_num_divisible_brute():
    num_not_found = True
    num = 1
    while num_not_found:
        divisible_by_all = True
        for i in range(min, max+1):
            if num % i != 0:
                divisible_by_all = False
                break
        if divisible_by_all:
            return num
        num += 1

""" old
def smallest_num_divisible_fast():
    all_factors = list()
    for i in range(min, max + 1):
        factors_of_i = get_factors(i)
        print(i, factors_of_i)
        for factor in factors_of_i:
            if factor not in all_factors:
                all_factors.append(factor)
    
    print(all_factors)
    
    # multiply each factor in list to get the smallest factor
    # divisible by min to max
    smallest_factor_of_all = 1
    for factor in all_factors:
        smallest_factor_of_all *= factor
    
    return smallest_factor_of_all

"""

def smallest_num_divisible_fast():
    all_factors = {}
    for i in range(min, max + 1):
        factors_of_i = get_factors(i)
        freq_of_factors = Counter(factors_of_i)
        print(i, factors_of_i, freq_of_factors)
        for factor in freq_of_factors:
            if factor not in all_factors:
                all_factors[factor] = freq_of_factors[factor]
            else:
                if freq_of_factors[factor] > all_factors[factor]:
                    all_factors[factor] = freq_of_factors[factor]
    
    print(all_factors)
    
    # multiply each factor in list to get the smallest factor
    # divisible by min to max
    smallest_factor_of_all = 1
    for factor in all_factors:
        # check if EVENLY divisble
        print(factor)
        smallest_factor_of_all *= factor * all_factors[factor]
    
    return smallest_factor_of_all

# debug function to check if all the numbers from min to max are divisble by given number.
def check(num):
    for i in range(min, max + 1):
        if num % i != 0:
            print(i, 'didn\'t work.')
        print('done.')



"""
def smallest_num_divisible_fast(min, max):
    - create a new list var called all_factors
    - get factor of every number, and while iterating,
        check if the numbers in the list of factors is in all_factors,
        if not, then include it
    - multiply all_factors by iterating through it and return that.

    x error: i also have to make sure that the frequency of each number is
        the same or greater than in each list.
    - find frequency of numbers in factors_of_i
    - for each number in factors_of_i, check in all_factors if
        the same frequency or greater exists.
        if not, then add the same freqency. * perhaps use a dictionary instead?

"""
    

print(smallest_num_divisible_fast())
        