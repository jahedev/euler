import sys
sys.setrecursionlimit(1500000)

def prim(n, x):
	if n%x != 0:
		return prim(n, x + 1)
	elif n/2 > x:
		print(x)
		return prim(n/x, x)
	else:
		return x

import time

start = time.process_time() # to measure time taken
lpn = prim(600851475143, 2)
time_taken = ((time.process_time() - start)*1000)

# print(get_factors(num))
print("Largest Prime Number:", lpn)

print('That took: ',"%.3f" % time_taken, 'miliseconds')