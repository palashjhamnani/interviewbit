import time
import math


# Two methods to check weather a number is prime or not
# First: Check division with every number less than itself
# Second: Check division with every number less than its square root

t1 = time.time()
i = 2
#N = 1000033
# Make N very large, the First approach won't give an answer, it will take a lot of time due to large input size and time complexity

N = 1500450271
#while i < N:
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


#To test time difference
#t1 = time.time()
#time.sleep(2)
#t2 = time.time()
#t = t2-t1
#print t
