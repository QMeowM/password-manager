from tkinter import *

window = Tk()
window.title("Sandbox Playground for Colummnspan")
# window.config()

r = Label(width=20, height=5, bg="red")
r.grid(row=0, column=0)
g = Label(width=20, height=5, bg="green")
g.grid(row=1, column=1)
b = Label(width=40, height=5, bg="blue")
b.grid(row=2, column=0, columnspan=2)

window.mainloop()