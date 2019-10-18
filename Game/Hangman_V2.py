from tkinter import *
# from PIL import ImageTk, Image
import tkinter.messagebox
window = Tk()

window.geometry('700x500')
window.title('Hangman Version 2 by BIG JIMMY')



def print1():
    print('fuck you')


label2 = Label(window,height=8,text = print1())
label2.grid(row = 0, column = 0, columnspan = 15)

btn01 = Button(window,text=" ",bg="white",fg="black", width=2,height=2,font=('Helvetica','20'),command = print1)
btn01.grid(column=7,row=0, columnspan = 20)
btn02 = Button(window,text=" ",bg="white",fg="black", width=2,height=2,font=('Helvetica','20'),command = print1)
btn02.grid(column=8,row=0, columnspan = 3)
btn03 = Button(window,text=" ",bg="white",fg="black", width=2,height=2,font=('Helvetica','20'),command = print1)
btn03.grid(column=9,row=0,columnspan = 3)
btn04 = Button(window,text=" ",bg="white",fg="black", width=2,height=2,font=('Helvetica','20'),command = print1)
btn04.grid(column=10,row=0, columnspan = 3)




btn1 = Button(window,text="Q",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'),command = print1)
btn1.grid(column=10,row=1)
btn2 = Button(window,text="W",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn2.grid(column=11,row=1)
btn3 = Button(window,text="E",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn3.grid(column=12,row=1)
btn4 = Button(window,text="R",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn4.grid(column=13,row=1)
btn5= Button(window,text="T",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn5.grid(column=14,row=1)
btn6= Button(window,text="Y",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn6.grid(column=16,row=1)
btn7 = Button(window,text="U",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn7.grid(column=17,row=1)
btn8 = Button(window,text="I",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn8.grid(column=18,row=1)
btn9 = Button(window,text="O",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn9.grid(column=19,row=1)
btn10 = Button(window,text="P",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn10.grid(column=20,row=1)






btn11 = Button(window,text="A",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn11.grid(column=11,row=2)
btn12 = Button(window,text="S",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn12.grid(column=12,row=2)
btn13= Button(window,text="D",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn13.grid(column=13,row=2)
btn14 = Button(window,text="F",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn14.grid(column=14,row=2)
btn15 = Button(window,text="G",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn15.grid(column=15,row=2)
btn16 = Button(window,text="H",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn16.grid(column=16,row=2)
btn17 = Button(window,text="J",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn17.grid(column=17,row=2)
btn18= Button(window,text="K",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn18.grid(column=18,row=2)
btn19= Button(window,text="L",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn19.grid(column=19,row=2)


btn20 = Button(window,text="Z",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn20.grid(column=3,row=3)
btn21 = Button(window,text="X",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn21.grid(column=4,row=3)
btn22 = Button(window,text="C",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn22.grid(column=5,row=3)
btn23= Button(window,text="V",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn23.grid(column=6,row=3)
btn24 = Button(window,text="B",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn24.grid(column=7,row=3)
btn25 = Button(window,text="N",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn25.grid(column=8,row=3)
btn26 = Button(window,text="M",bg="navy",fg="White", width=2,height=2,font=('Helvetica','15'))
btn26.grid(column=9,row=3)



label1 = Label(window,text="Guesses n stuff og thingss sofvn; sofjvn;sfvklns'lfkvn",fg="red",font=('Helvetica','12'))
label1.grid(row = 7, column = 0, columnspan = 15)
window.mainloop()