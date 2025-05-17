from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("500x500")
window.configure(background = "red")

def convert_temperature():
    celsius = e1.get()
    if (celsius.replace(".", "" , 1).isdigit()):
        fahrenheit = (float(celsius) * 9/5) + 32
        l3.config(text = "Temperature in Fahrenheit: " + str(fahrenheit))


l1 = Label(window, text = "Celsius -> Fahrenheit", font = ("Arial", 35))
l1.pack(padx = 15, pady = 10)

f1 = Frame(window, bg = "grey", padx = 70, pady = 70)
f1.pack(padx = 30, pady = 30)

l2 = Label(f1, text = "Enter temperature in Celsius", font = ("consolas 10 bold", 12))
l2.grid(row = 0, column = 0)

e1 = Entry(f1)
e1.grid(row = 0, column = 1, padx = 15, pady = 30)

b1 = Button(f1, text = "Convert", font = font.Font(size = 10, weight = "bold"),command = convert_temperature)
b1.grid(row = 1, column = 0, columnspan = 2, pady = 15)

l3 = Label(f1, width = 28, font = ("Arial", 17), fg = "Blue")
l3.grid(row = 2, column = 0 , columnspan = 2, pady = 15)





window.mainloop()

