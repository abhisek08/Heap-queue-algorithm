'''
 Write a Python program to find the three smallest integers from a given list of numbers using Heap queue algorithm.
'''
import heapq
l=[4,3,6,2,1,6,7,4,10,93,21,34]
print(heapq.nsmallest(3,l))