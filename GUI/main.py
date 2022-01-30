from tkinter import *
import random

root = Tk()
root.geometry("600x500")
root.config(bg='#222222')
root.title("Rock, Paper, Scissors!")
root.iconbitmap('e:/Codes/Python/Rock-Paper-Scissors/icon.ico')

choices = ["Rock", "Paper", "Scissors"]

points = 0
i = 0

def check_mode(btnFrame):

    btnFrame.grid_forget()

    btnFrame2 = Frame(root, bg='#222')
    bo3Btn = Button(btnFrame2, text="Best of 3", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: game(3, i,points, btnFrame2, choices))
    bo5Btn = Button(btnFrame2, text="Best of 5", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: game(5, i,points, btnFrame2, choices))
    quitBtn2 = Button(btnFrame2, text="quit", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=root.quit)

    bo3Btn.pack(side=LEFT,padx=20,pady=10)
    bo5Btn.pack(side=LEFT,padx=20, pady=10)
    quitBtn2.pack(side=RIGHT,padx=50, pady=10)
    btnFrame2.grid(row=4, column=3)
    
    onHover(bo3Btn,'green','#222')
    onHover(bo5Btn,'green','#222')
    onHover(quitBtn2,'red','#222')



def game(n, i, points, frame, choices):

    h = n//2 + 1

    frame.grid_forget()
    var = StringVar()

    btnFrame3 = Frame(root, bg='#222')
    rock = Button(btnFrame3, text="Play Rock", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: var.set("Rock"))
    paper = Button(btnFrame3, text="Play Paper", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: var.set("Paper"))
    scissors = Button(btnFrame3, text="Play Scissors", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: var.set("Scissors"))

    rock.pack(side=LEFT,padx=20,pady=10)
    paper.pack(side=LEFT,padx=20, pady=10)
    scissors.pack(side=RIGHT,padx=20, pady=10)
    btnFrame3.grid(row=5, column=3)
    
    onHover(rock,'brown','#222')
    onHover(paper,'gray','#222')
    onHover(scissors,'dark blue','#222')

    roundFrame = Frame(root, bg='#222')
    roundLabel = Label(roundFrame, text="", font=("Courier New Bold", 10), bg='#222', fg='#fff',justify=CENTER)
    roundLabel.pack()
    roundFrame.grid(row=4, column=3)

    roundFrame2 = Frame(root, bg='#222')
    roundLabel21 = Label(roundFrame2, text="", font=("Courier New Italic", 10), bg='#222', fg='#fff',justify=CENTER)
    roundLabel22 = Label(roundFrame2, text="", font=("Courier New Italic", 10), bg='#222', fg='#fff',justify=CENTER)
    roundLabel23 = Label(roundFrame2, text="", font=("Courier New", 10), bg='#222', fg='#fff',justify=CENTER)
    roundLabel24 = Label(roundFrame2, text="", font=("Courier New Bold", 10), bg='#222', fg='#fff',justify=CENTER)
    roundLabel21.pack()
    roundLabel22.pack()
    roundLabel23.pack()
    roundLabel24.pack()
    roundFrame2.grid(row=3, column=3)

    while i < n:

        roundLabel['text'] = "Playing Round " + str(i+1)

        btnFrame3.wait_variable(var)

        user = var.get()

        pc = random.choice(choices)

        i, points, res = play(i, points, user, pc)

        roundLabel21['text'] = "Your Choice: " + user
        roundLabel22['text'] = "PC Choice: " + pc
        roundLabel23['text'] = "\nYour Points: " + str(points)

        if res == -1:
            roundLabel24['text'] = "\nRound Lost :("
        if res == 0:
            roundLabel24['text'] = "\nIt's a Draw. Replaying Round " + str(i+1) + " ..."
        if res == 1:
            roundLabel24['text'] = "\nRound Won!"

        var = StringVar()


    roundFrame.grid_forget()
    roundFrame2.grid_forget()
    btnFrame3.grid_forget()
    resultFrame = Frame(root, bg='#222')
    resultLabel = Label(resultFrame, text="Your Score: " + str(points) + "/" + str(n), font=("Courier New Italic", 15), bg='#222', fg='#fff',justify=CENTER)
    resultLabel1 = Label(resultFrame, text="", font=("Courier New Bold", 15), bg='#222', fg='#fff',justify=CENTER)
    homeBtn = Button(resultFrame, text="Home", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: gohome(resultFrame))
    homeBtn.pack(side=BOTTOM)
    resultLabel.pack()
    resultLabel1.pack()

    onHover(homeBtn, 'gray', '#222')

    if points >= h:
        resultLabel1['text'] = "\nYou Win!\n"
    else:
        resultLabel1['text'] = "\nYou Lose :(\n"
    resultFrame.grid(row=3, column=3)


def gohome(resultFrame):

    resultFrame.grid_forget()
    start()



def play(i, points, user, pc):

    res = -1

    if user == pc :
        i -= 1
        res = 0
    elif user == "Rock" and pc == "Scissors":
        points += 1
        res = 1
    elif user == "Paper" and pc == "Rock":
        points += 1
        res = 1
    elif user == "Scissors" and pc == "Paper":
        points += 1
        res = 1
    
    i += 1

    return i, points, res
        

def onHover(button, colorOnHover, colorOnLeave):
  
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def start():

    myLabel = Label(root, text="Rock, Paper, Scissors!", font=("Courier New", 25), bg='#222', fg='#fff',justify=CENTER)
    myLabel2 = Label(root, text="from Mukunth BS", font=("Courier New Italic", 10), bg='#222', fg='#fff',justify=CENTER)

    myLabel.grid(row=1, column=3)
    myLabel2.grid(row=2, column=3)

    btnFrame = Frame(root, bg='#222')


    startBtn = Button(btnFrame, text="START", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=lambda: check_mode(btnFrame))
    quitBtn = Button(btnFrame, text="quit", padx=5, pady=5, font=("Courier New Bold", 12), borderwidth=1, bg='#222', fg='#fff', command=root.quit)

    startBtn.pack(side=LEFT,padx=50,pady=10)
    quitBtn.pack(side=RIGHT,padx=50, pady=10)

    btnFrame.grid(row=4, column=3)

    onHover(startBtn,'green','#222')
    onHover(quitBtn,'red','#222')

    n_rows = 7
    n_columns = 7
    for j in range(n_rows):
        root.grid_rowconfigure(j, weight = 1)
    for j in range(n_columns):
        root.grid_columnconfigure(j, weight = 1)
            
    root.mainloop() 

start()