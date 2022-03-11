import tkinter as tk

window = tk.Tk()
window.config(background='blue')

colourList = ['black', 'white']
rowCount = 0

def dambord():
    for repeat in range(5):
        columns('forwards')
        columns('backwards')


def columns(volgorde):
    global rowCount
    if volgorde == 'forwards':
        status = 0
    elif volgorde == 'backwards':
        status = 1
    
    for columns in range(10):
        label = tk.Label(background=colourList[status])
        label.config(padx=30,pady=25)
        label.grid(row=rowCount,column=columns)
        if status == 0:
            status = 1
        elif status == 1:
            status = 0
    rowCount += 1
    


dambord()

window.mainloop()