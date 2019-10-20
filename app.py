import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps=[]

#Button function
def addApp():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(("executables","*.app"),("all files","*.*"))
    )
    apps.append(filename)
    print(filename)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

#creating a frame inside or gui
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8 ,relheight=0.8, relx=0.1, rely=0.1)

#adding buttoms
openFile = tk.Button(
    root, text="Open File",
    padx=10, pady=5,
    bg="white",fg="#263D42",
    command=addApp
    )

openFile.pack()

runApps = tk.Button(
    root, text="Run",
    padx=10, pady=5,
    bg="white", fg="#263D42"
)
runApps.pack()
#to run the app and state open
root.mainloop()