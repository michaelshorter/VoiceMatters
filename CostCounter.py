import tkinter as tk
from tkinter import *

Cost = 9

def Cost_label(label):
    def count():
        global Cost
        Cost += 0.0002
        Cost4D = round(Cost, 2)             #convert number to 4 decimal places
        label.config(text="€" +str(Cost4D))     #display 4 decimal place total preceeded with a pound sign
        label.after(1000, count)

    count()

root = tk.Tk()
root.title("The Cost of Speech to Text")
root.geometry("1500x1000")
root.configure(bg='#AB4F98')
#root.configure(fg='#E73E55')

label = tk.Label(root, fg="white", font=('The Led Display St', 160), background="#AB4F98",)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
#label.pack()
Cost_label(label)
root.mainloop()
