import time

def pbar(string, curr, cap):
    print('\r %s %.2f%s \r' % (string,(curr/cap)*100,'%'), end='\r')

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def is_prime(n):

    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    # We store the number of factors in this variable
    factors = 0
    # This will loop from 1 to n
    for i in range(1, n+1):
        # Check if `i` divides `n`, if yes then we increment the factors
        if n % i == 0:
            factors += 1
    # If total factors are exactly 2
    if factors == 2:
        return True
    return False


def check_primes(prime_list):
    not_primes = []
    count = 0
    for num in prime_list:
        if not is_prime(num):
            not_primes.append(num)
        count += 1
        printProgressBar(count, len(prime_list), prefix = 'Checking Primes:', suffix = '', length = 50)
    
    if len(not_primes) == 0:
        print('All numbers in list are primes.')
    else:
        print('The following numbers are not prime:')
        print(not_primes)


for i in range(2,20000000):
    printProgressBar(i, 20000000, prefix = 'Checking Primes:', suffix = '', length = 50)

print()