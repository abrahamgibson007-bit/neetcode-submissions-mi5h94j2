class ListNode: 
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
# defines the building block of your linked list 
# each node stores a value and pointers to neigbors 
# is the constructor with default values

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0) # creates dummy head sentinel node 
        self.tail = ListNode(0) # creates dummy tail sentinel node
        self.head.next = self.tail # links head's next to tail, meaining an empty list has head -> tail and no real elements in between 
        self.tail.prev = self.head # links tail's prev to head, completes the doubly structure 
        self.size = 0 # tracks how many real elements are getting stored
# List initialization - defines the data structure 
# this class must support all the required operations 

 

    def getPrev(self, index: int) -> ListNode: # returns the node just before the target index 
        if index <= self.size // 2: # decides whether to traverse forward from the head or backwards from the tail
            cur = self.head # starts from the head when the target is in the first half
            for _ in range(index): # iteration 
                cur = cur.next
        else: 
            cur = self.tail # handles indices closer to the end by starting from the tail sentinel instead 
            for _ in range(self.size - index + 1): # walk backwards from tail for just enough steps to land on the predecessor of the index-th node 
                cur = cur.prev
        return cur

    def get(self, index: int) -> int: # get operation
        if index >= self.size: # checks bounds
            return -1
        return self.getPrev(index).next.val # finds the node at the index by getting its predecessor and then movuing one step forward

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None: # general insertion method
        if index > self.size:
            return
        node = ListNode(val) # creates the new node with the given value and null 
        prev = self.getPrev(index) # finds predecessor node should be inserted after 
        next = prev.next # is the mode currently at position index, which will become the next neighbor of the new node
        prev.next = node # rewires the predecessor's next pointer to the new node instead of the old
        node.prev = prev # sets the new node's prev pointer back to the predecessor 
        node.next = next # connects the new node forward to what used to be prev.next
        next.prev = node # completes the bidirectional link by pointing the next node's prev back to the new node 
        self.size += 1 # increments node count 

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: # rejects invalid indices
            return
        prev = self.getPrev(index) # gets node from immediately before the one to delete 
        cur = prev.next # the node you want to remove 
        next = cur.next # the node after the one you want to remove 
        prev.next = next # bypasses cur by linking the predecessor directly to the next node 
        next.prev = prev # completes the bypass in the other direction 
        self.size -= 1 # increments node count