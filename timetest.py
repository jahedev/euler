import time
import sys

start = time.process_time()
__import__(sys.argv[1])
time_taken = ((time.process_time() - start)*1000)
unit = 'miliseconds'

if time_taken / 1000 > 1.0:
    time_taken /= 1000
    unit = 'seconds'
    if time_taken / 60 > 1.0:
        time_taken /= 60
        unit = 'minutes'
        if time_taken / 60 > 1.0:
            time_taken /= 60
            unit = 'hours'


print('That took: ',"%.3f" % time_taken, unit)
