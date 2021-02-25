from nodes_linked_lists import *

class Hash_table():

    def __init__(self, initial_size):
        self.index_list=[]
        for i in range(initial_size):
            s = Singly_linked_list()
            self.index_list.append(s)

    def __key_to_ind__(self, key):
        hash_code = hash(key)
        index = hash(key)%len(self.index_list)
        #print(index)
        return index

    def __enter_value__(self, key):
        index = self.__key_to_ind__(key)
        self.index_list[index].__add_tail__(key)

    #returns all keys at an index
    def __show_all_at_index__(self, index):
        self.index_list[index].__return_all_nodes__()
        return

    def __lookup__(self, key):
        index = self.__key_to_ind__(key)
        print(index)
        return index
