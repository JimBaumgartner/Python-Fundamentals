

    def add_badge(self, to_add):
        if isinstance(to_add, Item):
            self.contents.append(to_add)
        else:
            to_add = False
        return to_add

    def read(self):
        return f'Menu: { self.contents }'   

class Door_access:

    def __init__(self):
        