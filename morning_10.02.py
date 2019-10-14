# Fill out the truth table
# a       b       not (a and b or b)
# ----------------------------------
# False   False     True
# True    False     True
# False   True      False
# True    True      False
# ========================================
# Each student that has an A in their name, print their age.
# Make your program able to handle any list of students (this format below)



students = [("AJ", 25), ("XD", 19), ("JA", 27), ("IS", 27)]

for a, b in students: #seperateing touple (or unpacking)
    # if a.lower() == "a"  #this one looks in the first position only
    if "a" in a.lower():  # this one looks in the whole, first half of the touple
        print(a, " is" , b)


# or 

# for a , b in students:
#     print((a, "is", b))  if "a" in a.lower() =="a"