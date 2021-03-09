from nodes_linked_lists import*

#O(N), where N is the size of list
#uses hash dictionary and a spare list structure
def removedups_1(singly_ll):
    result_list = Singly_linked_list()
    dictionary = {}
    #traverse singlelinked
    current = singly_ll.head
    while current!= None:
        if current.data not in dictionary:
            #add this to dictionary and new list
            x = {current.data:1}
            dictionary.update(x)
            result_list.__add_tail__(current.data)
        current = current.next
    return result_list

# previous, current, current.next
#current, current.next, current.next.next
#reassign the next link to skip the duplicates
#no additional list but memory gaps???
#still O(N)
def removedups_2(singly_ll):
    dictionary = {}
    previous = singly_ll.head
    current = previous.next
    #SKIPPED HEAD -- separately:
    if previous == None:
        return
    else:
        x = {previous.data:1}
        dictionary.update(x)

    while current!= None:
        if current.data not in dictionary:
            #add this to dictionary
            x = {current.data:1}
            dictionary.update(x)
            previous = current
        else:
            previous.next=current.next
        current = current.next
    return singly_ll
'''
by buffer they meant hash table
'''

#Having access only to the node:
#get address of the next one
#make pointer to that address
#instead of mynode, store the pointer at my address
#id() returns the object’s memory address.
#need to clear the true next one's address
'''
Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12. You only have access to the 9 node. Can you make it look like the correct answer?
'''

#returns value instead of node object... why???
#can't test without it
'''def find_node_in_sll(sll, node_data):
    current = sll.head.next
    while current is not sll.tail:
        if current.data == node_data:
            return str(current)
        current=current.next
    return str(current)'''

def delete_middle_node(node_object):
    if node_object== None or node_object.next == None:
        return False
    node_object.data = node_object.next.data
    node_object.next = node_object.next.next
    return True


#def sum_lists(list1, list2):
    #traverse both at the same time from head
    #sum
    #store sum
    #reverse lists
    #return
