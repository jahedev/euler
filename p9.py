"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

def find_abc_1000():
    for a in range(2,1100):
        for b in range(2,1100):
            for c in range(2,1100):
                if a < b:
                    if b < c:
                        a_2 = math.pow(a,2)
                        b_2 = math.pow(b,2)
                        c_2 = math.pow(c,2)
                        if a_2 + b_2 == c_2:
                            if (a + b + c) == 1000:
                                return({'set':(a,b,c),'product':a*b*c})

print(find_abc_1000())