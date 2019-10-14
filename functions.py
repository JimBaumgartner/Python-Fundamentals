# what are functions?
##  A function is a block of reusable code that can take in information and return information


# def FUNCTION_NAME_HERE(x): #parameters
#     print(x) #print whatever is being held in x
#     # Code Block
#     # any function can go here
#     return "some data"

# FUNCTION_NAME_HERE('parameter data')
# print(FUNCTION_NAME_HERE("Python is cool"))

# something = FUNCTION_NAME_HERE("I'm Data Too")
# print(something)


# multiple parameters


# def cash_register(total, tendered):
#     answer = ""
#     if tendered < total:
#         return "Hey your broke you owe me more"
#     elif tendered == total:
#         return "Have a nice Day"
#     else:
#         return "I owe you some money"       
# answer = cash_register(67,30)
# print(answer)


# default return statement

def combine(x,y,z):
    """
    Takes 3 numbers and prints their sum    
    """
    print(x+y+z)

what_is_this = combine(1,-2,3)# assigning intergers to combine and assigning combine to a variable
print(what_is_this) # print that variable assigned above


