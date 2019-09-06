"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# sum of even fibs below 4 million.

fib_seq=""
last_n=0
current_n=0

i = 1

last_n = 1
current_n = 1
fib_seq += str(current_n)

sum_of_even=0

while (current_n + last_n) < 4000000:
    tmp_n = current_n
    current_n = current_n + last_n
    last_n = tmp_n

    if current_n % 2 == 0:
        sum_of_even += current_n

    fib_seq += ", " + str(current_n)
    
    i += 1

print('Fibonacci Sequence: ', fib_seq)
print('Sum of Even Terms: ', sum_of_even) # 4613732

