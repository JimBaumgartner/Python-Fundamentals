#10.08.2019  Custom Data Types
    # we are building a list from scratch
"""
    Schematic for our Unordered List
    UnorderedList()         -> creates a new empty unordered list
    add(item)               -> adds an item to the front of the list
    remove(item)            -> removes the specified item from the list
    search(item)            -> searches the list for the item specified
    is_empty()              -> Returns if the list is empty or not
    length()                -> Returns the length of the list
    append(item)            -> Adds an item to the end of the list
    index(item)             -> returns the position of the item
    insert(position, item)  -> inserts an item in the list at the index
    pop()                   -> removes the item at the end of the list
    pop(index)              -> removes item at specified index
    """
class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'{self.data} -> {self.next}'
    
    def get_data(self):
        return self.data
    def edit_data(self, new_value):
        self.data = new_value
    def get_next(self):
        return self.next  # will return the next node to use later  
    def set_next(self, next_node):
        self.next = next_node

