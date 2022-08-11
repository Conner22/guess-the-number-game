from random import randint
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter as ttk

root = tk.Tk()

root.title('Number Guessing Game')
root.geometry('400x400+50+50')
root.iconphoto(False, tk.PhotoImage(file='random/numpic2.png'))



stuff = ttk.Frame(root)
stuff.pack(padx=10., pady=10, fill='x', expand=True)

choice = tk.StringVar()
result = '...'
num = randint(0,100)
hiddennum = 'idk'




def game():
    global num
    choice2 = f'{guess.get()}'

    num2 = int(num)
    choice3 = int(choice2)

    if choice3 == num2:
        done['text'] = 'You guessed correctly!'
        num = randint(0,100)
    elif choice3 != num2:
        done['text'] = 'You guessed incorrectly, try again'   
    else:
        print('error')

    num4 = str(num)

    if len(num4) == 3:
        hiddennum = '***'
        number['text'] = hiddennum
    elif len(num4) == 2:
        hiddennum = '**'
        number['text'] = hiddennum
    elif len(num4) == 1:
        hiddennum = '*'
        number['text'] = hiddennum
    else:
        print('error')


def giveans():
    anslabel['text'] = num


guess = ttk.Entry(stuff, textvariable=choice)
guess.pack()

number = ttk.Label(stuff, text='?')
number.pack()

button = ttk.Button(stuff, text="Click here to confirm answer", command=game)
button.pack()

done = ttk.Label(stuff, text=result)
done.pack()

spacer = ttk.Label(stuff, text='')
spacer.pack()

spacer2 = ttk.Label(stuff, text='')
spacer2.pack()

ansbutton = ttk.Button(stuff, text='Stuck? Press here for the number', command=giveans)
ansbutton.pack()

anslabel = ttk.Label(stuff, text='...')
anslabel.pack()


root.mainloop()
