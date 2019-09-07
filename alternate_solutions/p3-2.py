import time
import math


start = time.process_time() ###





x = 600851475143
i = 2
Result = []
while x != 1:
    if x % i == 0:
        x = math.floor(x / i)
        Result.append(i)
    i = i + 1


print((time.process_time() - start)*1000, 'miliseconds') ###