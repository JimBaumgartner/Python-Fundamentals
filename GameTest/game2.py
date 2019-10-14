import random
import images
import time

answer_list=[]
used = []
totalTime = .5
word_list = ['DOG','CAT']
bad_names = ['Pumpkin Spice', 'Cup Cake', ' Fart Breath', 'Dummy']
answer = random.choice(word_list)
new_name = random.choice(bad_names)
name = input(' Who dares challange me?  ' ).upper()
display = []
display.extend(answer)
used_letters.extend(display)
count = 0 

while count < len(answer)+5: 
    guess = input('Pleaase give me your guess    =====>   ').upper()
    print(count)

    for i in range (len(answer)):
        if answer[i] == guess :
            display[i] = guess
            count = count + 1
            used.remove(guess)
    
    if guess not in display:
        incorrect = incorrect - 1
        print('Sorry dude, thats wrong!!  you have ' , incorrect, 'left' )


    print(' '.join(display))
    print()


if count == len(answer)+5: 
    print('Well done dude, you guessed it' )
else:
    print('Sorry Dude,  Game over!!!')