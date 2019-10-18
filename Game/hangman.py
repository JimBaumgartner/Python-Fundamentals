import random
import time
from hangman_images import   full_hangman
from hangman_images import   hangman_base
from hangman_images import   hangman2
from hangman_images import   hangman3
from hangman_images import   hangman4

answer_list = ['DOG','CAT', 'COW', 'ALIGATOR' 'BIRD']  # list of answer 
bad_names = ['Pumpkin Spice', 'Cup Cake', ' Fart Breath', 'Dummy']  # list of insulting names
display = []  #createing a blank list 
used_letters = [] #createing a blank list  for all of the guesses
answer = random.choice(answer_list) # function (random) to choose something from the answer_list and asigning it a name of answer
new_name = random.choice(bad_names) # function (random) to choose something from the bad_names and asigning it a name of new_name
display.extend(answer) # this takes display[] list and seperates it into individual letters  D , O , G
totalTime = .75 # globaL variable seting delay time to half second

name = input(' Who dares challange me? ======>  ' ).upper()
time.sleep(totalTime)
print(f' \n ok { name } lets play some hangman  \n  ' )
time.sleep(totalTime)
print(f'You know what, I dont like the name { name }\n \n So I will now call you { new_name.upper() }  \n\n ' )
time.sleep(totalTime)
print(f'The answer has { len(answer) } letters \n\n ' )
time.sleep(totalTime)
print(f'The catagory is ANIMALS,     Thats the only hint you will get  \n \n' )
time.sleep(totalTime)
print(f'You Have 5 incorrect  guesses so good luck \n  \n')

for i in range (len(display)):
    display[i] = "_"

print(' '.join(display))

count = 0   # setting count to 0
incorrect = 5  # setting incorrect answers limit to 5

while count < len(answer) and incorrect > 0:
    guess = input('Pleaase give me your guess    =====>   ').upper()

    for i in range (len(answer)) :
        if answer[i] == guess:
            display[i] = guess
            count = count + 1
            print(f' You got lucky!!' ,guess, ' is in there ')
            print(' '.join(display))

    if guess not in display:
        used_letters.append(guess) # adding the incorect guess to list used_letters
        print(f' You have used these letters ===>  ' ,used_letters, )
        print(' '.join(display))
        incorrect = incorrect - 1 #counter for incorrect guesses decending by 1   
        if incorrect >0: # This line allows the below to print untill they have 1 guess left
            print('Sorry dude, thats wrong!!  you have ' , incorrect, 'guesses left' )
        if incorrect == 4: ##  nested if statement to call images from othe file.
            hangman_base()
        elif incorrect == 3:
            hangman2()
        elif incorrect == 2:
            hangman3()
        elif incorrect == 1:
            hangman4()

if count == len(answer): 
    print('Well done dude, you guessed it' )
else:
    print('Sorry Dude,  Game over!!!  The word was ',answer, )
    full_hangman()



