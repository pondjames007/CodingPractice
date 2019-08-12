# TIPS:
#
# Sol1:
# Merge Sort
# Top-Down
# Split the list into 2 parts using fast/slow pointers (when the fast pointer reach the end, the slow pointer is at middle)
# Recursively sort the 2 split lists (O(logn))
# And merge 2 split lists (O(n))
# T: O(nlogn)
# S: O(logn) (since the recursive depth is logn)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        mid = slow.next
        slow.next = None
        
        return self.merge(self.sortList(head), self.sortList(mid))
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val > l2.val: 
                l1, l2 = l2, l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            
        if l1: tail.next = l1
        if l2: tail.next = l2
        
        return dummy.next


# Sol2:
# Merge Sort
# Bottom-Up
# log(n) rounds, in the i-th round, we split the list into n/(2^i) lists (n, n/2, n/4, ...), each group has 2^(i-1) elements
# Merge every pair of sorted lists
# T: O(nlogn)
# S: O(1)
# Use iteration to simulate Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 0 or 1 element, we are done
        if not head or not head.next: return head
        
        len_ = 1
        cur = head
        while cur:
            cur = cur.next
            len_ += 1 
            
        dummy = ListNode(0)
        dummy.next = head
        
        n = 1
        while n < len_:
            cur = dummy.next # partial sorted head
            tail = dummy
            while cur:
                l = cur
                r = self.split(l, n)
                cur = self.split(r, n)
                tail.next, tail = self.merge(l, r)
                
            n <<= 1
            
        
        return dummy.next
    
    # split the list into 2 parts, first n element and the rest
    # return the head of the rest
    def split(self, head, n):
        n -= 1
        while(n and head):
            n -= 1
            head = head.next
        
        rest = head.next if head else None
        if head: head.next = None
        
        return rest
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            
        tail.next = l1 if l1 else l2
        while tail.next: tail = tail.next
        
        return dummy.next, tail  