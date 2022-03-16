import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime
from calendar import month_name
from calendar import day_name

var = datetime.today().strftime('%d-%m-%Y')
print(var)
days31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Okt', 'Dec']
days30 = ['Apr', 'Jun', 'Sep', 'Nov']
days28 = ['Feb']

root = tk.Tk()
root.title("Days by date calculator")
root.resizable(False, False)
root.geometry('300x200')

datelabel = tk.Label(text="Date:", font=('Helvetica', 19))
datelabel.pack(padx=60,pady=40)
datelabel.place(x=120,y=40)

def gapCreation(positionX):  
    gaplabel = tk.Label(text="-", font=19)
    gaplabel.pack()
    gaplabel.place(x=positionX,y=85)


def monthSelectEvent(event):
    print(event)
    chosenMonth = month_cb.get()
    daycomboboxset(chosenMonth)
    print(chosenMonth)


def daycomboboxset(comparison):
    if comparison in days31:
        day_cb['values'] = [[d] for d in range(1,32)]
    elif comparison in days30:
        day_cb['values'] = [[d] for d in range(1,31)]
    elif comparison in days28:
        day_cb['values'] = [[d] for d in range(1,29)]


def calculation():
    startday = day_cb.get()
    startmonth = month_cb.get()
    startyear = year_entry.get()
    print(startday)
    print(startmonth)
    print(startyear)


selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month, width=7)
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]
month_cb['state'] = 'readonly'
preselectMonth = datetime.today().strftime('%m')
preselectMonth = preselectMonth[1]
if preselectMonth.isdigit() == True:
    preselectMonth = int(preselectMonth)
    preselectMonth -= 1
convertingvar = month_cb['values'][preselectMonth]
month_cb.current(preselectMonth)
month_cb.pack(padx=40,pady=20)
month_cb.place(x=115,y=90)
month_cb.bind('<<ComboboxSelected>>', monthSelectEvent)

gapCreation(90)

selected_day = tk.StringVar()
day_cb = ttk.Combobox(root, textvariable=selected_day, width=7)
day_cb['state'] = 'readonly'
day_cb.pack(padx=40,pady=20)
day_cb.place(x=15,y=90)
daycomboboxset(convertingvar)
preselectday = datetime.today().strftime('%d')
preselectday = int(preselectday)
preselectday -= 1
day_cb.current(preselectday)

gapCreation(190)

year_entry = tk.Entry(width=7)
year_entry.pack(padx=40,pady=20)
year_entry.set(year_entry.get()[:4])
currentYear = datetime.today().strftime('%Y')
year_entry.insert(0,currentYear)
year_entry.place(x=210,y=90)

button = tk.Button(text='Calculate', command=calculation)
button.pack(ipadx=10,ipady=10)
button.place(x=120,y=150)


root.mainloop()