import tkinter as tk
from functools import partial
import random
from tkinter.messagebox import askyesno

window = tk.Tk()
window.geometry("1000x500")
window.config(bg="blue")
window.title("FPS Trainer V1")
timer = 20
points = 0
bindingList = ["<w>", "<a>", "<s>", "<d>", "<space>", "<Button-1>", "<Double-Button-1>", "<Triple-Button-1>"]
printTask = ["press: w", "press: a", "press: s", "press: d", "press: space", "Single click", "Double click", "Triple click", ]

def startupGame(startButton):
    global timer
    secondsInput = seconds_entry.get()
    if secondsInput.isdigit():
        timer = int(secondsInput)
    else:
        return None
    startButton.destroy()
    seconds_label.destroy()
    seconds_entry.destroy()
    window.config(bg="gray")
    labelScore.after(1000, time)
    runGame()


def runGame():
    chosenTaskposition = random.randrange(0,8)
    createButton(chosenTaskposition)



def time():
    global timer
    timer -= 1
    labelScore.config(text=("Time remaining: " + str(timer) + "                                                                                                         " + "Points: " + str(points)), font=("arial", 12))
    if timer == 0:
        window.after(2000, popupMSG)
    else:
        labelScore.after(1000, time)


def createButton(position):
    if timer > 0:
        xCord = random.randrange(50,950)
        yCord = random.randrange(100,450)
        button = tk.Button()
        button.config(text=printTask[position])
        button.pack(ipadx=10, ipady=10)
        button.place(x=xCord,y=yCord)
        if position <= 5:
            window.bind(bindingList[position], partial(PressedClicked, position, button))
        else:
            button.bind(bindingList[position], partial(PressedClicked, position, button))


def popupMSG():
    global timer
    global points
    anwser = askyesno(title="Game over", message=("Uw score was: " + str(points) + " punten. Wilt u opnieuw spelen?"))
    if anwser == False:
        window.destroy()
    elif anwser == True:
        window.config(bg="blue")
        timer = 20
        points = 0
        labelScore.config(bg="black", fg="white", text=("Time remaining: " + str(timer) + "                                                                                                         " + "Points: " + str(points)), font=("arial", 12))
        startButton = tk.Button()
        startButton.config(text="Click here to start", command=partial(startupGame, startButton))
        startButton.pack(ipadx=50, ipady=10, expand=True)
        seconds_label = tk.Label(text="Adjust ammout seconds:")
        seconds_label.pack(ipadx=50)
        seconds_entry = tk.Entry(justify='center')
        seconds_entry.pack(ipadx=50)
        seconds_entry.insert(0,)


def PressedClicked(position, givenButton, self):
    global points
    points += 1
    if position <= 5:
        window.unbind(bindingList[position])
    else:
        givenButton.unbind(bindingList[position])
    givenButton.destroy()
    runGame()
    


labelScore = tk.Label()
labelScore.config(bg="black", fg="white", text=("Time remaining: " + str(timer) + "                                                                                                         " + "Points: " + str(points)), font=("arial", 12))
labelScore.pack(ipadx=10, ipady=15, fill='x')

startButton = tk.Button()
startButton.config(text="Click here to start", command=partial(startupGame, startButton))
startButton.pack(ipadx=50, ipady=10, expand=True)

seconds_label = tk.Label(text="Adjust ammout seconds:")
seconds_label.pack(ipadx=50)

seconds_entry = tk.Entry(justify='center')
seconds_entry.pack(ipadx=50)
seconds_entry.insert(0,"20")

window.mainloop()