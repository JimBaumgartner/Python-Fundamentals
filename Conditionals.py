# A conditional resolves to a Boolean statement( true or False)

left = True
right = False

left == True  # == is equal to

right != "train" # != is not equal to

left is not right  #

# Equality Operators
left != right  #left and right are not equivalent
left == right   # left and right are equivalent
left is right   # left andf right are same identy
left is not right # Left and right are same identity

age_1 = 23
age_2 = 45


# Comparison Operators

age_1 > age_2   # left is greater than right
age_1 < age_2      # right is greater
age_1 >= age_2      # 
age_1 <= age_2

# logical Operators
age_1   ==  4 and age_2 < 22  #  and operator ( true ) and (false)
age_1 ==  4 or age_2 < 22   # or operator
not age_1  == 23

#a              b               a and b
#----------------------------------------
#True           True            True
#True           False           False
#False          True            False
#False          False           False


#a              b               a or b
#----------------------------------------
# True          True            True
# True          False           True
# False         True            True
# False         False           False

#a             not a
#--------------------
# True          False
# False         True

# x = 3
# name = "Ryan"

# if x > 3 and name == "Ryan":
#     if True:
#         print("I'm inside of an if if statement")
#     print("X is pretty big , and the person's name is ryan")
# elif x <= 3:
#     print("Maybe X is BIG?  who knows")
# else:
#     print("Otherwise, NO")

# Challange

# take a name and age, and if the person is under 18, say " Name  you are not and adult" 
# if the person is 18 but not 21, you say " You are an adult but not quite yet"
# if the Person is 21 or older , say  You are finally an adult
# if their name starts with an A say "cool name"
# case (12 , 18, 20, 21, 89)


age = int(input("What is your age? > "))
name = "Adam"
if age < 18:   # trick would go with "in range(18)", looks from 0 to ()
    print(f"{ name }, You are not an adult")
elif age >17 and age < 21 :
    print("You are an adult, but not quite yet")
elif age > 20 and (name[:1])  == "A":
    print("Cool Name By the way")
elif age > 20 :
    print(name, "You are fully and adult")


you = "Person"
you.replace("r",  "f")
print(you)


if name[0].lower() == "a":
    print("Cool Name Dude")    

# ranges   name[0:1]
#   name(0)


# declare a number
# if the number is divisible by  3, print "Fiz"
 #if the number is divisible by  5, print "Buzz"
 # if the number is divisible by both 3 & 5 , print "FizzBuzz"

 #Test cases 1, 3, 5, 10, 15, 98
number = 1

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)