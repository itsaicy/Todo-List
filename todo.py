from tkinter import *
import random
from PIL import Image, ImageTk

window = Tk()
image = Image.open("todo.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(window, text="", font=("Arial", 35, "italic"),
              bg="#8F9779", fg="white", image=photo)

label.grid(row=0, column=0, sticky="we")
window.geometry("450x450")

window.mainloop()