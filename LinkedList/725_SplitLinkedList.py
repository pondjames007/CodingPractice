# TIPS:
# Use second pointer/listnode variable to save the previous node so that when the part end it can be assign the next to be NONE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length = 0
        ptr = root
        while ptr:
            length += 1
            ptr = ptr.next
            
        num_ele = length // k
        remain = length % k
        
        ans = [None] * k
        head = root
        prev = None
        for i in range(k):
            ans[i] = head
            for j in range(num_ele + (1 if i < remain else 0)):
                prev = head
                head = head.next
            if prev: prev.next = None
        
        return ans
        
        