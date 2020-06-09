'''
Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm.
'''
import heapq
l=[4,3,6,2,1,6,7,4,10,93,21,34]
heapq.heapify(l)
print(l,type(l))