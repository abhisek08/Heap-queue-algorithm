'''
Write a Python program to compute maximum product of three numbers of a given array of integers using Heap queue algorithm.
'''
import heapq,functools
l=[4,3,6,2,1,6,7,4,10,93,21,34]
c=heapq.nlargest(3,l)
d=functools.reduce(lambda a,b:a*b,c)
print(d)