import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess, sys


root = tk.Tk()
apps=[]

#adding file save app
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        print(tempApps)

#Button function
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(("executables","*.app"),("all files","*.*"))
    )
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,
        bg="gray")
        label.pack()

def runApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener,app])


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
    bg="white", fg="#263D42",
    command=runApps
)
runApps.pack()
#to run the app and state open
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')