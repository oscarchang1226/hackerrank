from typing import List

'''
You want to move N items in k days (N >= k). You have to move at least one item
per day.
The items are listed in array P, where P[i] is size of item i.
You can move item i only if all items from 0 to [i - 1] are already moved.
Every day you need a container to pack the item and move it. The container size
needed for the day i is the maximum item size moved on that day.
Given k days and array P as the item sizes, find out the minimum total container
size required to move all the items.
'''

def maximumBoundedArray(itemSizes: List[int], days: int) -> int:
    return 0
