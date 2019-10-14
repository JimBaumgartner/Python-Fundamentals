num_1 = 7.5 
num_2 = 6.5
print(num_1//num_2)  # if you use print(int(num_1//num/2)),  this will get rid of decimal
#because it is changeing it to an int

event =input("What Type of event? > ")
guests = int(input("How many people will be there? > "))
if guests < 25:
    print("Not gonna work my friend, not enough people")
elif guests in range[25:30] and event == ("Wedding"):
    print("That we can do")