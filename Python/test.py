'''from node import *
from linked_lists import *

sll = Singly_linked_list()

for i in range(10):
    node = Node(i)
    sll.__add_tail__(node)

print(sll.__return_all_nodes__())
