from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import string

def caps(event):
    entryword.set(entryword.get().upper())


def wordcontrol():
    check = wordentrybox.get()
    if check.isalpha() == False:
        messagebox.showerror('Foutmelding','Alleen letters zijn toegestaan!!!')
    elif len(check) > 7:
        messagebox.showerror('Foutmelding','Het ingevulde woord is te groot!!!')
    elif len(check) < 4:
        messagebox.showerror('Foutmelding','Het ingevulde woord is te klein!!!')
    else:
        player2(check)


def player2(player1word):
    window1.destroy()
    window2 = tk.Tk()
    window2.title("Raad het woord - Player 2")
    window2.geometry("350x300")
    window2.config(bg='white')
    window2.resizable(False, False)
    wordlabel = tk.Label(window2, text="Raad het woord:", font=('Helvetica', 19), bg='white')
    wordlabel.pack(ipadx=10, ipady=10, fill='x')
    spinboxgenerate(window2, player1word)

    window2.mainloop()


def spinboxgenerate(window2, chosenword):
    alphabet = list(string.ascii_uppercase)
    lengthWord = len(chosenword)
    valueList = []
    widthfill = 7
    gapfill = 40
    timesnumber = 70
    for adjustment in range(4,8):
        if lengthWord == adjustment:
            break
        else:
            widthfill -= 1
            gapfill -= 10
            timesnumber -= 10
    for times in range(lengthWord):
        valueList.append(chosenword[times])
        var = StringVar(window2)
        var.set(valueList[times])
        spin_box = ttk.Spinbox(window2, values=alphabet, textvariable=var, wrap=True, state='readonly', width=widthfill)
        spin_box.place(y=150, x=(gapfill+(times*timesnumber)))


window1 = tk.Tk()
window1.title("Raad het woord - Player 1")
window1.geometry("350x300")
window1.config(bg='white')
window1.resizable(False, False)

guesswordlabel = tk.Label(text="Vul een woord in:", font=('Helvetica', 19), bg='white')
guesswordlabel.pack(ipadx=10, ipady=10, fill='x')

entryword = StringVar()
wordentrybox = tk.Entry(bg='white', font=('Helvetica', 15), justify='center', textvariable=entryword)
wordentrybox.bind("<KeyRelease>", caps)
wordentrybox.pack(ipadx=10, ipady=10)

wordlengthlabel = tk.Label(text="(4 tot 7 letters)", font=('Helvetica', 12), bg='white')
wordlengthlabel.pack(ipadx=10, ipady=10, fill='x')        

comfirmationbutton = tk.Button(text="Stel woord in", command=wordcontrol)
comfirmationbutton.pack(ipadx=10, ipady=10)

window1.mainloop()