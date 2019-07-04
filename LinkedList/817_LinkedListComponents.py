# TIPS:
# change the list G into a set
# go through the LinkedList and check the group from the set
# kick out the node from the set

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if len(G) == 1: return 1
        
        set_G = set(G)
        flag = True
        count = 0
        while head:
            if not set_G: return count
            
            if head.val in set_G:
                set_G.discard(head.val)
                if flag == True:
                    count += 1
                    flag = False
            else:
                flag = True
            
            head = head.next
        
        return count