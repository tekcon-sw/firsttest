#!/usr/bin/python
import time
import os

print 'Hello World!!'
print(os.environ('USERNAME'))

a = 0
while a < 1000:
    a += 1 # Same as a = a + 1 
    print (a)
    time.sleep(5)
