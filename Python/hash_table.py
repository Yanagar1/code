import linked_lists

class Hash_table(initial_size):
    def __init__(self):
        for i in range(initial_size):
            s = Singly_linked_list()
            index_list = [s]*initial_size

    def key_to_ind(key):
        hash_code = hash(key)
        index = hash(key)%len(index_list)
        return index

    def __enter_value__(self, key):
        index = key_to_ind(key)
        index_list[index].__add_tail__(key)

    #returns all keys at an index
    def __lookup__(self, key):
        index = key_to_ind(key)
        index_list[index].__return_all_nodes__()
        return
