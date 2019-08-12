# TIPS:
#
# Use HEAP
# add idx to break the equal val between 2 linked lists
# can also used in array (need to remember which array it comes from)
# k lists, each list has length n
# T: O(nklogk)
# S: O(k) + O(n) (if you copy the list) 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        heapq.heapify(heap)
        
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
            
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            _, i, smallest = heapq.heappop(heap)
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, i, smallest.next))
            
            tail.next = smallest
            tail = tail.next
            tail.next = None
            
        return dummy.next


# Divide & Conquer
# Use #021(mergeTwoLists)
# k lists, each list has length n
# T: O(nklogk)
# S: O(logk) (if use recursion) -> O(1) (if use iteration)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists)-1)
    
    
    
    def merge(self, lists, l, r):
        if l > r: return None
        if l == r: return lists[l]
        if l+1 == r: return self.mergeTwoLists(lists[l], lists[r])
        
        mid = (l+r)//2
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid+1, r)
        
        return self.mergeTwoLists(l1, l2)
    
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        
        # make sure the first node
        if l1.val <= l2.val:
            ans = l1
            l1 = l1.next
        else:
            ans = l2
            l2 = l2.next
        
        node = ans
        
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        
        if l1: node.next = l1
        if l2: node.next = l2
            
        return ans