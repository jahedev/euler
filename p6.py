"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import math

natural_numbers_100 = list(range(1,101))

sum_of_sqares = 0

for i in natural_numbers_100:
    sum_of_sqares += math.pow(i, 2)

sum = 0 # of the first hundred natural numbers

for i in natural_numbers_100:
    sum += i

sqare_of_sum = math.pow(sum, 2)

diff = int(sqare_of_sum - sum_of_sqares)
print(diff)