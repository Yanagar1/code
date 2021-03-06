from nodes_linked_lists import*


def removedups(singly_ll):
    result_list = SinglyLinkedList
    dictionary = {}
    #traverse singlelinked
    current = singly_ll.head
    while current!= None:
        if current.data not in dictionary:
            #add this to dictionary and new list
            x = {current.data:1}
            dictionary.update{x}
            result_list.__add_tail__(current.data)
        current = current.next
    return result_list

# previous, current, current.next
#current, current.next, current.next.next
def removedups(singly_ll):
    dictionary = {}
    previous = singly_ll.head
    current = previous.next
    #SKIPPED HEAD -- separately:
    if previous == None:
        return
    else:
        x = {previous.data:1}
        dictionary.update{x}

    while current!= None:
        if current.data not in dictionary:
            #add this to dictionary and new list
            x = {current.data:1}
            dictionary.update{x}
            previous = current
        else:
            previous.next=current.next
        current = current.next
    return singly_ll
'''
'''

def delete_middle_node(singly_ll, data):
#the first met instance of the data
#not consider head
#traverse and keep the previous
    previous = singly_ll.head
    current = previous.next

    while current!= None:
        if current.data != data:
            previous = current
        else:
            previous.next=current.next
        current = current.next
    return
'''
Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12. You only have access to the 9 node. Can you make it look like the correct answer?
'''
#Having access only to the node:
#get address of the next one
#make pointer to that address
#instead of mynode, store the pointer at my address
#id() returns the object’s memory address.
#need to clear the true next one's address
def delete_node(node_object):
    node_object = node_object.next
    return


def sum_lists(list1, list2):
    #traverse both at the same time from head
    #sum
    #store sum
    #reverse lists
