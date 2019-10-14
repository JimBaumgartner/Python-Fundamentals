# collections
# containers to store multiple objects or things
# List, Tuple, set

# List:
# CRUD
# create, read, update, delete

# my_list = [1,2,3]  #create
# first_item = my_list[0]  # read indexing
# my_slice = my_list[-2::] # read slicing
# my_slice = list(reversed(my_list[0])
# print(my_slice)

# my_list.append(['hello, world']) # update appends to the end
# my_list[1]= 6   #update  an index
# my_list.insert(1, 8)  #update something at location of 1
# my_list.pop()           # update removes the last item off the list
# my_list.pop(0)          # update removes the first item off 
#                         # you can capture what you pop off in a variable
#                         # it removes that item and returns the exact thing
# my_list                       
n = 10
while n >= 0:
	print (n , 'not yet')
	n -= 1
print("finally done")


my_dictionary = {
    "name" : "adam Jayne",
    "age"   :  25
}
my_dictionary["name"]                   # grabbing a value t the  'name' key
my_dictionary.get("name")               # gets a value of the name key
my_dictionary['name'] = "New_Name"      # update a value at the name key
my_dictionary["hobby"] = "Python"       # add a key value if the key dosent exist 
my_dictionary.update({'hobby': 'golf'}) #
my_dictionary.keys()    #grabs all the key values
my_dictionary.values()  # grabs all of the values
my_dictionary.items()   # grabs everthing in a tuple format

# # functions
# def function_name(<parameters>):
# # arguments are data objects passed ubto and held by the parameter names
# def change(X):
#     V = "VELICITY"
#     return x + 1
# change(12)
# print(v)



#Classes
# custom data type object that contains methods and attributes
# Class <class name here>(<inherited>) :

class Animal:

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def get_kingdom(self):
        return self.kingdom


class Human(Animal):            # Human now inherits Animal and all parameters
    def __init__(self, kingdom, name,age): 
        super().__init__(kingdom)  # pulls kingdom from above
        self.name = name
        self.age = age

    def  speak(self):
        return f'Hello, i am { self.name }'


me = Human("camlot",'jim',99)
print(me.get_kingdom())

