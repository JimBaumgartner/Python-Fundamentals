class Item:
    """
    Item class is a representation of menu item
    """
    def __init__(self,name,price):
        self.name = name
        self.price = price    
    def __repr__(self):
        return f'[ { self.name }, ${ self.price } ]'    
    def change_price(self, new_price):
        """
        This changes price of menu item
        """
        self.price = abs(new_price)
        return True

    def change_name(self, new_name):
        """
        This is to change to a new name
        """
        self.name = str(new_name)
        return True
class Menu:
    """
    a place to manage the menu
    """

    def __init__(self, contents=[]):
        self.contents = contents 
    def __repr__(self):
        return f'Menu: { self.contents }'
    def __str__(self):
        return f'Menu: { self.contents }'    
    def add_item(self, to_add):
        if isinstance(to_add, Item):
            self.contents.append(to_add)
        else:
            to_add = False
        return to_add
    
    def read(self):
        return f'Menu: { self.contents }'   
    def remove_item(self,to_remove):
        if to_remove in self.contents:
            index = self.contents.index(to_remove)
            self.contents.pop(index) 
        else:
            to_remove = False   
        return  to_remove
