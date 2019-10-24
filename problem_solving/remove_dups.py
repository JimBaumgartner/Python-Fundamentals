from ..unordered_list import UnorderedList # .. means going up a folder # calling Unordered list function from unorder_list folder

def remove_dups(linked_list):
    start = linked_list.head  # saying to start at head

    while start:
        my_next = start.get_next()
        
        while my_next:
            if start.get_data()  ==  my_next.get_next():
                start.get_next(my_next.get_next())
            my_next = my_next.get_next()

        start = start.get_next()


my_list = UnorderedList()
somestuff = [4,2,44,23,2,3,4,9]

for i in somestuff:
    my_list.add_item(i)

print(my_list.length()) 