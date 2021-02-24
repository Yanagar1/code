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


class Singly_linked_list(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __add_tail__(self, new_value):
        new_node = Node(new_value)
        if self.head == None:
            self.head = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
        self.tail = new_node
        return

    def __return_all_nodes__(self):
        ret = ()
        current = self.head
        while current!= self.tail:
            ret+=(current,)
            current = current.next
        ret+=(self.tail,)
        return ret


class DoublyLinkedList(SinglyLinkedList):

    def __init__(self):
        SinglyLinkedList.__init__(self)

    def __str__(self):
        return "<=>".join([str(i) for i in self])

    def add2Head (self, item):
        oldhead=self._head
        self._head = TwoWayNode(item, None, self._head)
        if oldhead == None:
            self._tail = self._head
        else:
            oldhead.previous = self._head

    def add2Tail(self, item):
        self._tail.next=TwoWayNode(item, None, self._tail)
        self._tail=self._tail.next
        if oldtail==None:
            self._head = self._tail
