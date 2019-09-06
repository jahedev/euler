import math

"""
fib(n) = Phi^n – ( (–1)^n)/Phi^n ) / math.sqrt(5)

ref: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section1
"""

def fib(n):
    Phi = (math.sqrt(5)+1)/2
    phi = Phi - 1
    return int((math.pow(Phi, n) - math.pow(phi*(-1), n)) / math.sqrt(5))

i = 1
current_term = 0
sum_of_even = 0

while fib(i) < 4000000:
    current_term = fib(i)
    i += 1

    if current_term % 2 == 0:
        sum_of_even += current_term

print(sum_of_even)

