#tinker = python built in libraray for GUI
import tkinter as tk
from tkinter import messagebox

#to check player is win 
#def means to define function

def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],[0,4,8],[2,4,6]]:

       #"" == "" == ""
       if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":

           #if player win , winning button green
           #.config() is use for change the button properties
           buttons[combo[0]].config(bg="green") #means background green
           buttons[combo[1]].config(bg="green") #means background green
           buttons[combo[2]].config(bg="green") #means background green

           #winner popup
           #f"" = string in python use for insert variable into string
           global winner
           winner = True
           messagebox.showinfo("Tic-Tac-Toe", f"Player{buttons[combo[0]]['text']} wins!=")
           root.quit() #for close game



def check_draw():
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "Match Draw!")
        root.quit()

           #for user turn 

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player

        check_winner()

        if not winner:
            check_draw()

        toggle_player()


def toggle_player(): #function use for switch the player
    global current_player
    current_player = "X" if current_player == "o" else "o"
    label.config(text=f"Player{current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

#create 9 button and store in list

buttons = [tk.Button(root, text="", font=("normal", 25), width = 6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

#buttons arrange in grid (3by3) shape

for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)

#current player variable

current_player = "X"

#winner variable for check game is going on or not
winner = False

label = tk.Label(root,text=f"Player{current_player}'s turn", font=("normal", 16))

root.mainloop()
