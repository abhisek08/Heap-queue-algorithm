'''
Write a Python program to delete the smallest element from the given Heap and then inserts a new item.
'''
import heapq
l=[4,3,6,2,1,6,7,4,10,93,21,34]
heapq.heapify(l)
heapq.heapreplace(l,0)
print(l)