#!/usr/bin/python
import time

print 'Hello World!!'
print os.environ.get('USERNAME')

a = 0
while a < 1000:
    a += 1 # Same as a = a + 1 
    print (a)
    time.sleep(5)
