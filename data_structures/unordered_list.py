# 10.08.2019  Custom DataTypes
# Nodes
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

class UnorderedList:

    def __init__(self):
        self.head = None # setting the head (it is none right now)

    def add_item(self,new_item): # adding a new node 
        temp = new_item  #creates new node
        temp.set_next(self.head) #sets new node to point to next( which is the very end)
        self.head = temp  # sets the new item (called temp)  to the head level

    def is_empty(self):
        return self.head == None

    def length(self):
        count = 0
        current = self.head

        while current != None:
            count += 1 
            current = current.get_next()

        return count

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data == item:
                found = True
            else:
                previous = current
                curent = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current

    def search(self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else :
                curent = current.get_next()

        return found

    def index(self,item):
        index = 0
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                curent = current.get_next()
                index += 1
        return index

                        
my_linked = UnorderedList()

my_linked.add_item(89)
my_linked.add_item('Hello')

print(my_linked.length())

my_linked.remove(89)

print(my_linked.length())

print(my_linked.search('Hell'))
print(my_linked.index('Hello'))