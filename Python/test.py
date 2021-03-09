from nodes_linked_lists import *
from chapter2 import*

test_list = Singly_linked_list()
test_list.__add_tail__("a")
test_list.__add_tail__("b")
test_list.__add_tail__("c")
test_list.__add_tail__("d")
print("HEAD", test_list.head.data)
print("TAIL", test_list.tail.data)

#test_list.__return_all_nodes__()

node_address = find_node_in_sll(test_list, "b")
print(node_address)
#delete_middle_node(node_address)
#test_list.__return_all_nodes__()
#print(test_list.head.data)
#print(test_list.tail.data)
