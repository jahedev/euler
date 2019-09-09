#!/usr/local/bin/python3

import time
import sys

start = time.process_time()
__import__(sys.argv[1])
time_taken = ((time.process_time() - start)*1000)

print('That took: ',"%.3f" % time_taken, 'miliseconds')
