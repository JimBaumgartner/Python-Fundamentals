while True:
    prompt = """
    Hello Security Admin:

    How can i help you?

    1) List all Badges
    2) Add a badge 
    3) Edit a badge.
    4) Exit
    =>>"""

option = int(input(prompt))
def read_menu(): # will be used in option 1
    return current_menu.read()

def create_badge(badgeid,access):
    new_badge = Badge(name, price)
    current_menu.add_item(new_item)
    return(f' { new_badge } succesfully added')

def add_badge(self, to_add):
        if isinstance(to_add, Item):
            self.contents.append(to_add)
        else:
            to_add = False
        return to_add




if option == 1: #list all badges
    print(read_menu())
elif option == 2: #adding badges
    new_badge_name = input(f'What badge would you like to add? ==> ')
    new_door_access = input(f'What door will this badge access? ==> ')
    print(add_badge(new_badge_name, new_door_access))
elif option == 4:
    quit




current_menu = Menu()

class Badges:
    
    def __init__(self,badgeid,access,access2):
        self.badgeid = badgeid
        self.access = access
        self.access2 = access2
    def __repr__(self):
        return f'Menu: { self.contents }'
    def __str__(self):
        return f'Menu: { self.contents }'   
    
    
    
    def add_badge(self, to_add):
        if isinstance(to_add, BadgeID):
            self.contents.append(to_add)
        else:
            to_add = False
        return to_add