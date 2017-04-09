import time
import math

t1 = time.time()
i = 2
#N = 1000033
N = 1500450271
while i < math.sqrt(N):
    if N % i == 0:
        print "Not prime"
        break
    else:
        if i == N-1:
            print "Prime"
        i = i+1

t2 = time.time()
t = t2-t1
print "Time taken = "+ str(t)+"Seconds"
