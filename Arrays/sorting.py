## SORTING ALGORITHMS IN PYTHON 2.7 ##

import time
import random

# This is for Randomly generating list with 10,000 integers.

def generate():
    a = random.sample(xrange(1, 10001), 10000)
    return a

# Selection Sort O(n^2):
# Here we SELECT minimum element from list and replace it with min index,
# and continue with the process untill the list is sorted.


def selection_sort(a):
    t1 = time.time()
    n = len(a)
    for i in range(0,n-1):
        imin = i
        # This second for loop checks for minimum element and updates imin.
        for j in range(i+1, n):
            if a[j]<a[imin]:
                imin = j
        # Here we swap a[i] with minimum element.
        temp = a[i]
        a[i] = a[imin]
        a[imin] = temp
    #print a
    t2 = time.time()
    print "Time for Selection Sort = "+str(t2-t1)


# Bubble Sort O(n^2):
# Here we scan the list, and compare adjacent elements and swap them if not in
# order, the maximum elements will bubble up at the end, and list will be sorted.

def bubble_sort(a):
    t1 = time.time()
    n = len(a)
    for j in range (0, n-1):
        # We set a flag, just to check if swap happens, if not, we break rather than keep checking.
        flag = 0
        # n-j-1, because we don't need to compare already sorted elements present at the end of list.
        for i in range(0, n-j-1):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                flag = 1
        if flag==0:
            break
    #print a
    t2 = time.time()
    print "Time for Bubble Sort = "+str(t2-t1)
    

    
def tim_sort(a):
    t1 = time.time()
    a = sorted(a)
    t2 = time.time()
    #print a
    print "Time for Python's internal Tim Sort = "+str(t2-t1)


#selection_sort(generate())
#bubble_sort(generate())
tim_sort(generate())
    
