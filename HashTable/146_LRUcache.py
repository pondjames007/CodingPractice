# TIPS:
# * collections.OrderedDict
# * Maybe LinkedList to store the order
# * How to implement without using OrderedDict?

from collections import OrderedDict
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value


# Implement LinkedList by yourself
class DLinkedList:
    def __init__(self):
        self.key  = 0
        self.val  = 0
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        
        self.head = DLinkedList()
        self.tail = DLinkedList()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        '''
        If the requested cache not exist return -1, otherwise, return it is value and
            move it to the top of the cache (to mark it as a latest visited so it will not be removed)
        '''
        if key not in self.cache:
            return -1
        requestedNode = self.cache[key]
        self.moveNodeToTop(requestedNode)
        
        return requestedNode.val

    def put(self, key: int, value: int) -> None:
        '''
        Add new node to the top of the head and if the cache capacity reached we just need to remove
            the least recently used cache and it will be at the end of course so remove it and add
            the new item to the top of the cache.
        But what if the node already there so just move it to the top, and you done.
        '''
        node = self.cache.get(key, None)
        if not node:
            newNode = DLinkedList()
            newNode.key = key
            newNode.val = value
            
            self.addNodeToTop(newNode)
            # store it in our cache
            self.cache[key] = newNode
            self.size += 1
            
            # if our cache size exceeds our capacity remove the least used cache
            if self.size > self.capacity:
                removedNode = self.removeLeastUsedNode()
                del self.cache[removedNode.key]
                self.size -= 1
        else:
            node.val = value
            self.moveNodeToTop(node)
    
    def addNodeToTop(self, node):
        '''
        Adding new node in the fron of the cache, latest accessed by client
        '''
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        '''
        Remove node from the list from any place
        '''
        prevNode = node.prev
        nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def moveNodeToTop(self, node):
        '''
        Move the latest accessed node to be in the beginning of the cache
        '''
        self.removeNode(node)
        self.addNodeToTop(node)
    
    def removeLeastUsedNode(self):
        '''
        Use this function to remove the least recently used node
        '''
        node = self.tail.prev
        self.removeNode(node)
        return node