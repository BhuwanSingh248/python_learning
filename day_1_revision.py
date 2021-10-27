# day 1 : pure python optimizations
'''
    * some operation with list are complex like inserting on 0th index can take order of O(n)
    * same with deletion python provide class for optimization "collection.deque" 
'''

from collections import deque
import collections
import queue

list_1 = deque()   # created deque object
print(list_1)
list_1.append(47)   # add element at last index 
list_1.append(12)   
list_1.insert(0, 2)  # add element at given index
list_1.appendleft(1)    # append element at index 0
print(list_1)

list_2 = list_1.copy() 
print(f"list 1 : {list_1} and list_2 : {list_2}")
list_2.clear()
print(f"list 2 after clear {list_2}")

list_2.append(0)
list_2.append(-1)
list_2.append(-2)

# -------------------------------------------------------------------------------
list_1.extendleft(list_2)
list_2.extend(list_1)
print("-----------------------------------------------------------------------")
print("new list are  ")
print(list_1)
print(list_2)
# -------------------------------------------------------------------------------


print(list_2.index(0, 3, 10))    # index(search_value, start_index, end_index)

# -------------------------------------------------------------------------------

# other functions 
'''
    # insert(index, value)     # index error after maxlen
    # pop()                    # index error for no element
    # popleft()                # index error for no element
    # remove(value)            # raise value error if not in the deque
    # reverse()                # return None
    # rotate(n=1)  # rotate n element to right and left if n is -ve
    # maxlen       #if bounded 

'''


#############################################################################

# index to add element in sorted array 

import bisect
collection = [1, 2, 4, 5, 6]
bisect.bisect(collection, 5)
# return index at which value can be entered inorder to keep array sorted


###########################################################################


# using heap for getting max value 

import heapq
collection = [10, 2, 3, 4, 5, 24, 19, 3]
heapq.heapify(collection)
print(collection)
print(heapq.heappop(collection))

# using PQs

from queue import PriorityQueue

collection = [10, 2, 3, 4, 5, 24, 19, 3]
queue = PriorityQueue()
for i in collection:
    queue.put(i)
print(queue.get())  # returns minimum element 

queue = PriorityQueue()
queue.put((1, "val 1"))   # put number with object can be used for processes
queue.put((2, "val 2"))
queue.put((3, "val 3"))

print(queue.get())