class Node:
    def __init__(self, next=None, prev=None, data=None):
         
        # reference to next node in DLL
        self.next = next
         
        # reference to previous node in DLL
        self.prev = prev
        self.data = data
