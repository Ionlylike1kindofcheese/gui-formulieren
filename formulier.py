import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import string

root = tk.Tk()
root.title("Marathon Regristratie Fomulier")
root.config(bg='blue')
root.resizable(False, False)
root.geometry('300x300')

welcomelabel = tk.Label(text="Regristratie fomulier:", font=('Helvetica', 24), bg='blue')
welcomelabel.place(y=40)

def startfomulier():
    global namebox
    global agebox
    global birtdatebox
    global checkbuttonvar
    global handinbutton
    root.config(bg='grey')
    welcomelabel.destroy()
    continuebutton.destroy()
    namelabel = tk.Label(root, text="Naam:", font=('Helvetica', 15), bg='gray')
    namelabel.place(x=30, y=30)
    namebox = tk.Entry()
    namebox.place(x=130, y=35)
    agelabel = tk.Label(root, text="Leeftijd:", font=('Helvetica', 15), bg='gray')
    agelabel.place(x=30, y=70)
    agebox = tk.Entry()
    agebox.place(x=130, y=75)
    birthdatelabel = tk.Label(root, text="Geboorte:", font=('Helvetica', 15), bg='gray')
    birthdatelabel.place(x=30,y=110)
    birtdatebox = tk.Entry()
    birtdatebox.place(x=130, y=115)
    checkbuttonvar = tk.IntVar()
    termscheck = tk.Checkbutton(root, text='Agree to all terms', variable=checkbuttonvar, onvalue=1, offvalue=0)
    termscheck.place(x=90,y=150)
    handinbutton = tk.Button(root, text="Formulier inleveren", command=checkformulier)
    handinbutton.place(x=90, y=230)


def checkformulier():
    namecheck = namebox.get()
    agecheck = agebox.get()
    birthdatecheck = birtdatebox.get()
    termscheck = checkbuttonvar.get()
    if namecheck.isalpha() == True and agecheck.isdigit() == True and '-' in birthdatecheck and termscheck == 1:
        showinfo(title="Formulier ingevuld", message="Uw gegevens zijn succesvol ingevuld")
        namebox.destroy()
        agebox.destroy()
        birtdatebox.destroy()
        handinbutton.destroy()
        coveruplabel = tk.Label(root, padx=70, pady=30, bg='gray')
        coveruplabel.place(x=90, y=150)
        showname = tk.Label(root, text=str(namecheck), font=('Helvetica', 15), bg='gray')
        showname.place(x=130, y=30)
        showage = tk.Label(root, text=str(agecheck), font=('Helvetica', 15), bg='gray')
        showage.place(x=130, y=70)
        showbirthdate = tk.Label(root, text=str(birthdatecheck), font=('Helvetica', 15), bg='gray')
        showbirthdate.place(x=130, y=110)
        generatedcode = codegenerator()
        codelabel = tk.Label(root, text=("Regristratiecode: " + generatedcode), font=('Helvetica', 15), bg='gray')
        codelabel.place(x=30, y=220)
    else:
        additionalmesg = ""
        if namecheck.isalpha() == False:
            additionalmesg = "Volledige naam is niet vereist maar gebruik geen spaties. Plak het anders aan elkaar met hoofdletter"
        elif agecheck.isdigit() == False:
            additionalmesg = "Voor de leeftijd hoef je alleen maar een nummer te gebruiken"
        elif '-' not in birtdatebox:
            additionalmesg = "Gebruik dit bij de geboortedatum: '-'. Schrijf de geboortdatum zo op: dag-maand-jaar"
        elif termscheck == 0:
            additionalmesg = "U ben vergeten de voorwaarden aan te vinken"
        messagebox.showerror(title="Foutmelding", message="Sommige gegevens kloppen niet. " + additionalmesg)


def codegenerator():
    letters = list(string.ascii_uppercase)
    numbers = []
    code = ""
    for x in range(10):
        numbers.append(x)
    for characters in range(6):
        chosenthing = random.randrange(0,2)
        if chosenthing == 0:
            chosenletter = random.choice(letters)
            code += str(chosenletter)
        elif chosenthing == 1:
            chosennumber = random.choice(numbers)
            code += str(chosennumber)
    return code
        

continuebutton = tk.Button(text='Klik hier', width=9, height=3, command=startfomulier)
continuebutton.place(x=110, y=170)



root.mainloop()