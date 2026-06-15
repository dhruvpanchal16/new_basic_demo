from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("300x400")

# Display box
entry = Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Function for button click
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

# Function to clear display
def clear():
    entry.delete(0, END)

# Function to calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Row 1
Button(root, text="7", width=5, height=2,
       command=lambda: click(7)).grid(row=1, column=0)

Button(root, text="8", width=5, height=2,
       command=lambda: click(8)).grid(row=1, column=1)

Button(root, text="9", width=5, height=2,
       command=lambda: click(9)).grid(row=1, column=2)

Button(root, text="/", width=5, height=2,
       command=lambda: click("/")).grid(row=1, column=3)

# Row 2
Button(root, text="4", width=5, height=2,
       command=lambda: click(4)).grid(row=2, column=0)

Button(root, text="5", width=5, height=2,
       command=lambda: click(5)).grid(row=2, column=1)

Button(root, text="6", width=5, height=2,
       command=lambda: click(6)).grid(row=2, column=2)

Button(root, text="*", width=5, height=2,
       command=lambda: click("*")).grid(row=2, column=3)

# Row 3
Button(root, text="1", width=5, height=2,
       command=lambda: click(1)).grid(row=3, column=0)

Button(root, text="2", width=5, height=2,
       command=lambda: click(2)).grid(row=3, column=1)

Button(root, text="3", width=5, height=2,
       command=lambda: click(3)).grid(row=3, column=2)

Button(root, text="-", width=5, height=2,
       command=lambda: click("-")).grid(row=3, column=3)

# Row 4
Button(root, text="0", width=5, height=2,
       command=lambda: click(0)).grid(row=4, column=0)

Button(root, text="C", width=5, height=2,
       command=clear).grid(row=4, column=1)

Button(root, text="=", width=5, height=2,
       command=equal).grid(row=4, column=2)

Button(root, text="+", width=5, height=2,
       command=lambda: click("+")).grid(row=4, column=3)

# Run program
root.mainloop()