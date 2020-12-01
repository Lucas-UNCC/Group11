import tkinter
from tkinter import *

window = tkinter.Tk()  # Create the window
window.title("Escape From Tarkov Profit Calculator") # Change The Window Name

tkinter.Label(window, text="Enter Unique Item Material Cost").grid(row=0) # First Line to enter

e1 = tkinter.Entry(window)
tkinter.Label(window, text="First Unique Item").grid(row=1)
e1.grid(row=1, column=1)

e2 = tkinter.Entry(window)
tkinter.Label(window, text="Second Unique Item").grid(row=2)
e2.grid(row=2, column=1)

e3 = tkinter.Entry(window)
tkinter.Label(window, text="Third Unique Item").grid(row=3)
e3.grid(row=3, column=1)

e4 = tkinter.Entry(window)
tkinter.Label(window, text="Fourth Unique Item").grid(row=4)
e4.grid(row=4, column=1)

product = tkinter.Entry(window)
tkinter.Label(window, text="Enter The Price of the Product from The Craft").grid(row=6)
product.grid(row=6, column=1)

minutes = tkinter.Entry(window)
tkinter.Label(window, text="Enter the Time in Minutes it Takes to Complete The Craft").grid(row=7)
minutes.grid(row=7, column=1)

def getProfit():
    saleprice = int(product.get())
    costToMake = int(e1.get()) + int(e2.get()) + int(e3.get()) + int(e4.get())
    profit = saleprice - costToMake
    epic = 'Your Profit is %d Roubles ' %profit
    tkinter.Label(window, text=epic).grid(row=9)

    time = float(minutes.get())
    pph = profit / time
    epic2 = 'Your Profit Per Hour is %d Roubles' %pph
    tkinter.Label(window,text=epic2).grid(row=10)


button = tkinter.Button(text="Calculate Profit", command=getProfit)
button.grid(row=8, column=1)


mainloop()
