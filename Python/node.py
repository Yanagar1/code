class Node(object):
    #Represents a singly linked node
    def __init__(self, data=None, next=None):
        """Initiates a Node with a default next of None."""
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if self is other: return True
        if type(self)!=type(other): return False
        if self.data!=other.data: return False
        if self.next is None: return other is None

class TwoWayNode(Node):
    #2-way node object for doubly linked list

    def __init__(self, data=None, previous=None, next=None):
        Node.__init__(self, data, next) #calling parent class constructor
        self.previous = previous
