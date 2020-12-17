import tkinter
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

import webbrowser

url = 'https://tarkov-market.com/' #Live Website Tracker

window = tkinter.Tk()  # Create the window

window.title("Escape From Tarkov Profit Calculator") # Change The Window Name

ttk.Label(window, text="Enter Unique Item Material Cost").grid(row=0) # First Line to enter

# Creating text prompt and entry window for the first item
e1 = ttk.Entry(window)
ttk.Label(window, text="First Unique Item").grid(row=1)
e1.grid(row=1, column=1)

#Create first quanity box
a1 = ttk.Entry(window)
ttk.Label(window, text="Amount").grid(row=1,column=2)
a1.grid(row=1, column=3)

# Creating text prompt and entry window for the second item
e2 = ttk.Entry(window)
ttk.Label(window, text="Second Unique Item").grid(row=2)
e2.grid(row=2, column=1)

a2 = ttk.Entry(window)
ttk.Label(window, text="Amount").grid(row=2,column=2)
a2.grid(row=2, column=3)

# Creating text prompt and entry window for the third item
e3 = ttk.Entry(window)
ttk.Label(window, text="Third Unique Item").grid(row=3)
e3.grid(row=3, column=1)

a3 = ttk.Entry(window)
ttk.Label(window, text="Amount").grid(row=3,column=2)
a3.grid(row=3, column=3)

# Creating text prompt and entry window for the fourth item
e4 = ttk.Entry(window)
ttk.Label(window, text="Fourth Unique Item").grid(row=4)
e4.grid(row=4, column=1)

a4 = ttk.Entry(window)
ttk.Label(window, text="Amount").grid(row=4,column=2)
a4.grid(row=4, column=3)

#Creating Text Prompt and entry window for the sale price of the item produced from the craft
product = ttk.Entry(window)
ttk.Label(window, text="Enter The Price of the Product from The Craft").grid(row=6)
product.grid(row=6, column=1)

#Creating Text Prompt and entry window for the time it takes to complete the craft
minutes = ttk.Entry(window)
ttk.Label(window, text="Enter the Time in Minutes it Takes to Complete The Craft").grid(row=7)
minutes.grid(row=7, column=1)

#Method to calculate profit
def getProfit():
    saleprice = int(product.get())
    costToMake = int(e1.get()) * int(a1.get()) + int(e2.get()) * int(a2.get()) + int(e3.get()) * int(a3.get()) + int(e4.get()) * int(a4.get())
    profit = saleprice - costToMake
    epic = 'Your Profit is %d Roubles ' %profit
    ttk.Label(window, text=epic).grid(row=9)

    time = float(minutes.get())
    pph = profit / time
    epic2 = 'Your Profit Per Hour is %d Roubles' %pph
    ttk.Label(window,text=epic2).grid(row=10)

def darkMode():
    window['background'] = '#414141'  # Dark Mode
    style = ThemedStyle(window)
    style.set_theme("equilux")

#Button that calls the profit method
button = ttk.Button(text="Calculate Profit", command=getProfit)
button.grid(row=8, column=1)

button = ttk.Button(text="Live Market", command = lambda : webbrowser.open_new_tab(url))
button.grid(row=11,column=1)

button = ttk.Button(text="Dark Mode", command=darkMode)
button.grid(row=12,column=1)
window.mainloop()




