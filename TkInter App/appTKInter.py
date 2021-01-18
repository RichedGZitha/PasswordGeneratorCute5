#!/bin/python

import generator
import tkinter as tk

from PIL import Image, ImageTk

# create a tk window.
root = tk.Tk()

# title of the window.
root.title("Password Generator")

# resizable(x,y).
root.resizable(False, False)

# create a canvas.
canvas = tk.Canvas(root,height=620, width=400, background="#263D42", highlightthickness=1)

# put something into canvas	
canvas.pack()

# create a frame.
frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

passwordFrame = tk.Frame(frame, bg ="white")
passwordFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

# Logo Image

# Slogan

# Background

# Result Here
passwordLabel = tk.Label(passwordFrame, text="Generated password will appear here.", padx=5, pady=100)
passwordLabel.pack(expand=1)

#rb = tk.Radiobutton(frame, value="No", padx=5, pady = 1, text ="Can you")
#rb.pack()
def copy():

	text = passLengthEntry.get()
	passLengthEntry.clipboard_append(text)
	#tk.Copy(text)
	#print(text)


passLengthLabel = tk.Label(frame, text="Enter the number of characters", pady=10)
passLengthLabel.pack()

passLengthEntry = tk.Entry(frame, bg="white", fg="#263D42", width=30)
passLengthEntry.pack(pady=10)

# update passowrd
def genPass():

	for label in passwordFrame.winfo_children():
		label.destroy()

	text = generator.generatePassword()
	#passwordLabel.__setitem__(self, "text", text)
	passwordLabel = tk.Label(passwordFrame, text=text, padx=0, pady=100, width= 30)
	passwordLabel.pack( expand=1)

	#e = tk.Entry(passwordFrame, width=30)
	#e.insert(0, text)
	#e.pack()

	copyButton = tk.Button(passwordFrame, text="Copy to clipboard", padx=5, pady=10, bg="#263D42", fg="white", command=copy)
	copyButton.pack()


# create a submit button
submitbutton = tk.Button(root, text="Generate a password", bg = '#263D42', fg="white",pady=10 , command= genPass)
submitbutton.pack()

if __name__ == "__main__":
	
	 # start, show the window.
	root.mainloop()
