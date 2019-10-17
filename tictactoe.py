from tkinter import *
from tkinter import messagebox

tk = Tk()

tk.title("Tic Tac Toe")

label = Label(tk, text="Player 1:", font="Times 15 bold", bg="white", fg="black", height=1, width=8)
label.grid(row=1, column=0)

label = Label(tk, text="Player 2:", font="Times 15 bold", bg="white", fg="black", height=1, width=8)
label.grid(row=2, column=0)

playera = StringVar()
playerb = StringVar()
player1 = StringVar()
player2 = StringVar()
buttons = StringVar()

player1_name = Entry(tk, textvariable=player1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=player2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

player_switch = True
flag = 0


button1 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button1))
button1.grid(row=3, column=0)


button2 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button2))
button2.grid(row=3, column=1)


button3 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button3))
button3.grid(row=3, column=2)


button4 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button4))
button4.grid(row=4, column=0)


button5 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button5))
button5.grid(row=4, column=1)


button6 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button6))
button6.grid(row=4, column=2)


button7 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button7))
button7.grid(row=5, column=0)


button8 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button8))
button8.grid(row=5, column=1)


button9 = Button(tk, text=" ", font="Times 20 bold", bg="black", fg="white", height=4, width=8,
                 command=lambda: button_click(button9))
button9.grid(row=5, column=2)


def disablebutton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def button_click(buttonz):
    global player_switch, flag, player2_name, player1_name, playerb, playera
    if buttonz["text"] == " " and player_switch is True:
        buttonz["text"] = "X"
        player_switch = False
        playerb = player2.get() + " Wins!"
        playera = player1.get() + " Wins!"
        check_win()
        flag += 1

    elif buttonz["text"] == " " and player_switch is False:
        buttonz["text"] = "O"
        player_switch = True
        check_win()
        flag += 1

    else:
        messagebox.showinfo("Tic-Tac-Toe", "Square already used")


def check_win():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        disablebutton()
        messagebox.showinfo("Tic-Tac-Toe", playera)

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        disablebutton()
        messagebox.showinfo("Tic-Tac-Toe", playerb)

    elif flag == 8:
        messagebox.showinfo("Tic-Tac-Toe", "TIE")


tk.mainloop()

