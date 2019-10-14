

# Bronze--  10/01/2019
# Create two variables containing floatsa and print the result of floor divison

# silver & gold
# Cateering service
# Prompt a user for an event type, and the number of guests attending
# if the event is a banquet, the min number of the attendents for the catering business to work the event is 30
# if the event is a werdding , the min number of attendents for thr catering to work is 25
# the catering business will not work any other events at this time
# when the num of attendents is below the min, display a msg that expr3esses there are too few people

# num_1 = 7.5 
# num_2 = 6.5
# print(num_1//num_2)  # if you use print(int(num_1//num/2)),  this will get rid of decimal
#because it is changeing it to an int
x = 25
y = 30

event =input("What Type of event? > ").lower()
guests = int(input("How many people will be there? > "))


if event != "banquet" and event.lower() != "wedding":
    print("We dont have that service avaliable for wedding")
elif event == "banquet" and guests < y:
    print("Not enough people for a banquet")
elif event == "wedding" and guests < x :
    print("not enough people to have a wedding")
else:
    print("you will have enough guests for the event")

