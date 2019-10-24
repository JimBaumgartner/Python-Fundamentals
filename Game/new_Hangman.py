from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

correct_gueses = 0
window = Tk()  #setting up main window 
answer_list = ['DOG','CAT','BIRD','COW','BAT', "ALIGATOR"]  # list of answer
window.title("Hangman Version 3,  Yes I said Version 3") # Setting title message
lblanswer=StringVar() #sets label 

#answer label
Label(window, textvariable= lblanswer, font = ('consolas 24 bold')).grid(row = 0,column = 0, columnspan = 10)
Label(window, textvariable= f'chances left' , font = ('consolas 24 bold')).grid(row =10,column = 0, columnspan = 10)

def game ():
    global answer_with_spaces
    global num_guesses  
    global answer
    num_guesses = 0
    messagebox.showwarning("Let me give you a hint!!!!!",  "      THINK ANIMALS      ")
    # imgLabel.config(image=photos[0])
    answer = random.choice(answer_list)
    answer_with_spaces='_'.join(answer)
    lblanswer.set(' '.join('_'*len(answer)))
    
def guess (letter):
    global num_guesses
    global answer
    global correct_gueses
    if num_guesses < len(answer)+5:
        txt = list(answer_with_spaces)
        guessed = list(lblanswer.get())
        if answer_with_spaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c]= letter
                    correct_gueses += 1
                lblanswer.set(''.join(guessed))
        if correct_gueses == len(answer):
            messagebox.showinfo("", "Well Done you guessed it")  
        else:
            num_guesses += 1                
            if num_guesses ==  len(answer)+5 :
                messagebox.showwarning("Really Dude???",  "    GAME OVER   ")

#keyboard structure
n = 0 # counter starts at 0
for c in ascii_uppercase: # for every instance in ascii uppercase, this will create a button
    Button(window, text=c, command = lambda c = c: guess(c) , font = ('helvitica 18'), width=4).grid(row = 1+n//9, column=n%9)
    n += 1 # after each button is created , counter advances +1 untill no more instances in ascii uppercase

#exit button structure and command, allows user to exit game any time
exit_button=Button(window, text="EXIT" , font = ('helvitica 18'), width=20, command=window.quit)
exit_button.grid(row = 10,column = 0, columnspan = 10, padx = 20, pady=40)

game() # calls for function game()  which is main game structure
window.mainloop()
