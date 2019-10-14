#Lambdas
adding = lambda x: x + 15

numbers = [ 1,2,3,4,5 ]
def add_15(val):
    return val + 15

# my_numbers = list(map(add_15, numbers))
# print(my_numbers)


# z = adding(15)
# print(z)

# my_numbers = list(map(add_15,numbers))
my_numbers = set(map(lambda  x : x+15, numbers))