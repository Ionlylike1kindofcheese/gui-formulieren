import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime
from calendar import month_name
from calendar import day_name

var = datetime.today().strftime('%d-%m-%Y')
print(var)

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

selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month, width=7)
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]
month_cb['state'] = 'readonly'
month_cb.pack(padx=40,pady=20)
month_cb.place(x=115,y=90)

gapCreation(90)

selected_day = tk.StringVar()
day_cb = ttk.Combobox(root, textvariable=selected_day, width=7)
day_cb['values'] = [[d] for d in range(1,32)]
day_cb['state'] = 'readonly'
day_cb.pack(padx=40,pady=20)
day_cb.place(x=15,y=90)

gapCreation(190)

year_entry = tk.Entry(width=7)
year_entry.pack(padx=40,pady=20)
year_entry.insert(0,...)
year_entry.place(x=210,y=90)


root.mainloop()