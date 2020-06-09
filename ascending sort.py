'''
 Write a Python program to sort a given list of elements in ascending order using Heap queue algorithm
'''
l=[4,3,6,2,1,6,7,4,10,93,21,34]
import heapq
heapq.heapify(l)
for i in range(len(l)):
    print(heapq.heappop(l),end=' ')