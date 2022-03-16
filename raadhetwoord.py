from tkinter import *
from tkinter import messagebox
import tkinter as tk

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
        ...

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