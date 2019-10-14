from datetime import datetime  # have to import this to make date time work correctly
import pprint  # importing pretty print module, justg allows me to print easier to read


class Human:
    earthian = True  # setting earthian to true  , dont know why


    def __init__(self, name,age,birthday):
        self.name = name
        self.age  = age
        self.birthday = birthday
   
    def have_birthday(self):  #defining have_birthday to self?
        self.age += 1   # this adds 1 to age
    
    def greet(self):  # defining greet at self level
            return f'Hello, my name is {self.name}' 

    def human_globals(self):
            return globals()

mini_me = Human("Carson", 0, datetime(year=2019, month=6,day=27))

# pprint.pprint(mini_me.__dict__)  # called pretty print to print globals 
                                #  __dict__ is printing an attribute of a class (human in this instance)
        
#or


#  pprint.pprint(dir())   # does exact same thing as (  pprint.pprint(mini_me.__dict__) )
                        # prints the dir of the attribute
#  pprint.pprint(dir("")) # prints the dir of the string

# purple ones are methods
# yellow are attrubutes

# help(Human)   # just help screen for class of Human
