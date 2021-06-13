from tkinter import *
from passwd import *

root = Tk()
root.title("Password Tester App")

def getData():
	passwd = ent.get()
	if lengthCheck(passwd) and charCheck(passwd) and upperCheck(passwd) and lowerCheck(passwd) and checkNum(passwd) and dictCheck(passwd) == True:
		result = Label(root, text=f"Your Password {passwd} is very strong", fg="red", bg="white")
		result.grid(row=3,column=1, padx=10, pady=10, columnspan=5)
		ent.delete(0, END)
	else:
		result = Label(root, text=f"Your Password {passwd} is not strong", fg="red", bg="white")
		result.grid(row=3,column=1, padx=10, pady=10, columnspan=5)
		ent.delete(0, END)


info = Label(root, text="Please enter your Password for testing", fg="green")
ent = Entry(root, width=30, bg="yellow")
subButton = Button(root, text="Enter", bg="white", command=getData)

info.grid(row=0,column=1, padx=5, pady=5)
ent.grid(row=1,column=1, padx=10, pady=10)
subButton.grid(row=2,column=1, padx=5, pady=5)


root.mainloop()
