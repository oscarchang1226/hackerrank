from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toArray(self) -> List:
        if self.val is None:
            return []
        l = [self.val]
        nextNode = self.next
        while nextNode is not None:
            l.append(nextNode.val)
            nextNode = nextNode.next
        return l
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        for i in lists:
            if i is None:
                continue
            l.append(i.val)
            while i.next:
                l.append(i.next.val)
                i = i.next
        l.sort()
        if (len(l) > 0):
            mergedList = ListNode(l[0])
            for i in l[1:]:
                nextNode = mergedList
                while nextNode.next is not None:
                    nextNode = nextNode.next
                nextNode.next = ListNode(i)
            return mergedList
        return None
