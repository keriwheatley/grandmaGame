#debug turned on
import pdb; pdb.set_trace()
import string
import time

def solution():
    print "Starting Collatz iterations."
    start_time = time.time()
    number = 1
    iterations = 1

    for i in range(1000000):

        z = i
        n=1

        #print "Starting number: ", i

        while z > 1:
            if z % 2 == 1:
                z = 3 * z + 1
                n=n + 1
                #print "Number is odd. New number: ", z, " Iteration: ", n
            else:
                z = z / 2
                n=n + 1
                #print "Number is even. New number: ", z, " Iteration: ", n

        if n > iterations:
            iterations = n
            number = i

    print "Number:", number, " Iterations:", iterations
    print("--- %s seconds ---" % (time.time() - start_time))

solution()

"""Longest Collatz sequence 

The following iterative sequence is defined for the set of positive integers: 
if n is even, n = n/2
if n is odd, n = 3n + 1
it ends when n = 1
"""

"""def solution():
    print "Starting Collatz iterations."
    start_time = time.time()
    stored_counts = {}

    for i in range(1000000):

        z = i

        n=0
        print "Starting number: ", i

        while z > 1:
            if z in stored_counts.keys():
                #print "Using stored factor. Current number:", z, " Current iteration:", n, " Stored iteration:", stored_counts[z]                
                n = n + stored_counts[z]
                del stored_counts[z]
                break
            if z % 2 == 1:
                z = 3 * z + 1
                n=n + 1
                #print "Number is odd. New number: ", z, " Iteration: ", n
            else:
                z = z / 2
                n=n + 1
                #print "Number is even. New number: ", z, " Iteration: ", n

        stored_counts[i] = n

    maximum = max(stored_counts, key=stored_counts.get)  # Just use 'min' instead of 'max' for minimum.

    print "Number:", maximum, " Iterations:", stored_counts[maximum]
    print("--- %s seconds ---" % (time.time() - start_time))"""
