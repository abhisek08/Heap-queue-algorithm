'''
Write a Python program to implement a heapsort by pushing all values onto a heap and then popping off the smallest values one at a time
'''
import heapq
l=[4,3,6,2,1,6,7,4,10,93,21,34]
h=[]
for i in l:
    heapq.heappush(h,i)
for i in range(len(h)):
    print(heapq.heappop(h))

