'''
Write a Python program to find the kth (1 <= k <= array's length) largest element in an unsorted array using Heap queue algorithm.
'''
import heapq
l=[4,3,6,2,1,6,7,4,10,93,21,34]
c=heapq.nlargest(3,l)
print(c[3-1])