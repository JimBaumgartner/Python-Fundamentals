#  10/01/2019


#  Loops
# For Loops

animals = ["Jaguar","Racoon","Fox","Cat","Toucan"]

for animals in animals: 
    print(animals)

#for( i=0; i<len(animals); i++)  this is C++ script (adruino)

for i in range(100):
    print(i)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif  i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#  nested for loop  
for i in range(30):
    for j in range(30):
        if i == j:
            print("they Match", i)



expenses = [("McDonalds",12.00),  # this is a list of touples
            ("Steam", 49.99),
            ("Rent", 900.00)
]

total = 0.00
for expense in expenses:
    total += expense[1]  # the [1] is to look inside the touple 
print(total)



# While loops


while (False):
    #code block
    print("Im in a while loop")

x = 0
while x < 100: # has to resolve as true
    print(x)
    
    if x == 92:
        break
else:
    print("While loop never ran")  


products = [ "nvidia", "amd", "arm", "intel", "risc"]
search_term = "risc"
#create a while loop that searches this list until it finds the search term

x = 0

while x < len(products)-1 and search_term != products[x]:
    x += 1
else:
    print("found", search_term, "at location", x)
    print(x)


# cheat way for while loop
if search_term in products:
    print(products.index(search_term))
else:
    print("Not Found")