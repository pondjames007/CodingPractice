# TIPS:
# * Set up a table to record next node


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head: 'ListNode') -> 'bool':
        if not head: return False
        
        table = {}

        while head.next:
            if head.next in table:
                return True
            table.setdefault(head, head.next)
            head = head.next
        return False