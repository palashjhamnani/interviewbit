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



# Insertion Sort, Best case O(n), Worst case O(n^2):
# Here we start inserting elements from the unsorted part to the sorted part of array


def insertion_sort(a):
    t1 = time.time()
    n = len(a)
    for i in range(1, n):
        value = a[i]
        hole = i
        while (hole>0 and a[hole-1]>value):
            a[hole] = a[hole-1]
            hole = hole-1
        a[hole] = value
    t2 = time.time()
    #print a
    print "Time for Insertion Sort = "+str(t2-t1)



# Merge Sort: O(nlogn), worst case - O(n^2), Not an in-place sorting algo(Space complexity = O(n).)
# Here we divide and conquer recursively.



def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


# Quick Sort: O(nlogn), worst case - O(n^2), in-place sorting.
# Here we select a pivot element and swap elements on both sides of the pivot based on their comparison with the pivot element itself.


def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)
    
    

# Tim sort is based on Python's internal sorted method (Fastest).


def tim_sort(a):
    t1 = time.time()
    a = sorted(a)
    t2 = time.time()
    #print a
    print "Time for Python's internal Tim Sort = "+str(t2-t1)




# EXECUTION: Uncomment blocks to test.


#selection_sort(generate())

#bubble_sort(generate())

#insertion_sort(generate())

#tim_sort(generate())

# Time measured externally dure to recursive calls

#t1 = time.time()
#merge_sort(generate())
#t2 = time.time()
#print "Time for Merge Sort = "+str(t2-t1)

#t1 = time.time()
#quicksort(generate())
#t2 = time.time()
#print "Time for Quick Sort = "+str(t2-t1)
