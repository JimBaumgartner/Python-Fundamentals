# 10/01/2019
# Lists
# list items can be of any type

names = ["Adam", "justin", "Xzavier"]
Students = [
    "The Rock",
    "Charles",
    "The undertaker",
    "Big Show",
    "Tony Stark",
    [
        "nested lists",
        "are cool",
            [
                56,
                100
            ]
    ]
]
print(names[0])
names.append("Jim")
print(names[-1])
print(Students[-1][-1][0])
names.insert(1, "Debbie")  # inserting a name into a list
print(names)

Students.extend(names)  # copies names list into studentrs file

names.pop() # this removes names in a list (go to this value and remove it)
print(Students)
print(len(Students))
Students.remove("Charles") # removes that exact name from that list (will remove the first one only)

# Slicing
#  Start : Stop : Step  # step is not inclusive
#[  0   :   3:    1  ]  ( to reverse the list use [0:0:-1])or [::-1]
 
new_list = Students[0:3:1]
print(new_list)
reversed_list = Students[::-1]
reversed_again = list(reversed(Students))
print(reversed_again)






# Tuples
# are like lists , except they are IMMUTABLE, you can slice a Tuple, what ever you 
#slice from a Tuple is a Tuple

my_tuple = (12,32)

print(my_tuple[0])

my_name = ("Adam","Jim")
f_name, l_name = my_tuple

tuple_names = ("Matthew", "Mark", "Luke", "John", "Judas")
something = tuple_names[3:5]
print(something)
tester = ("John")
print(tester)






#  Set
# unique items only
# sets are muttable
# a set is unordered , unique items, muttable, 
states = {"Indiana", "Alaska", "Texas"}

print(states)

states.add("Ohio")
states.remove("Alaska") # remove item, error if not there
states.discard("Indiana") # removes if there silently
#states.clear()          #  Clears whole set

print("Indiana" in states)   # this will produce a boolean  (true or false)








sentence = "Mary, had a little lamb"
list_of_words = sentence.split()
print(list_of_words)





my_names = ["Wallaby", "Bakersfield", "colGate", "COcaCOla"]

# remove colGate
# add Crest
# Change COcaCOla to lowercase
# grab every other item in list
# print each item individually
my_names.remove("colGate")
my_names.append("Crest")
my_names[2] = my_names[2].lower()  # changes to that position to lower case
print(my_names[:-1:2])  # grabs every other item on that list
print("\n".join(my_names))  #  trick to print seperate on its own line



