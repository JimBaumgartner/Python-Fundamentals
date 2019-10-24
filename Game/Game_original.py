import random

import time

answer_list=[]
used_letters=[]
totalTime = .5
word_list = ['DOG','CAT']
bad_names = ['Pumpkin Spice', 'Cup Cake', ' Fart Breath', 'Dummy']
answer = random.choice(word_list)
new_name = random.choice(bad_names)
name = input(' Who dares challange me?  ' ).upper()

time.sleep(totalTime)
print(f'ok { name } lets play some hangman  \n \n ' )
time.sleep(totalTime)
print(f'You know what, I dont like the name { name }\n \n So I will now call you { new_name.upper() }  \n\n ' )
time.sleep(totalTime)
print(f'The answer has { len(answer) } letters \n\n ' )
time.sleep(totalTime)
print(f'The catagory is ANIMALS,     Thats the only hint you will get  \n \n' )
time.sleep(totalTime)
print(f'You Have 5 incorrect  guesses so good luck \n  \n')

display = []
display.extend(answer)
print(display)

guess = input(f'Pick a letter ====> ').upper()
chances = len(answer) + 3
while chances > 0:
        
        if guess in answer:  
                chances -= 1    
                print('LUCKY GUESS  That one is in there >>>>>  ')    
        if guess not in answer:
                chances -= 1 
                used_letters.append(guess)
                print(f' You have { chances } guesses left' )
                print(f' you have used { used_letters } ' )
else:
        if chances == 0:
                print('Really Dude?')
                print("            I give up dude  \n "
                        "             GAME OVER!!!!          ")

