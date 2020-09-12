#Rennie Bevineau

from tkinter import *
frame = Tk()
frame.title("Change Counter")

Label(frame, text = "*****Enter the number of each type of coin and hit result******").grid(row=0,columnspan=4)

#create the labels for the coin types
Label(frame, text = "Dollar coins").grid(row=1,column=0)
Label(frame, text = "Half-Dollars").grid(row=2,column=0)
Label(frame, text = "Quarters").grid(row=3,column=0)
Label(frame, text = "Dimes").grid(row=4,column=0)
Label(frame, text = "Nickels").grid(row=5,column=0)
Label(frame, text = "Pennies").grid(row=6,column=0)

#create the input boxes for the coin types
dollars = Entry(frame)
halfDollars = Entry(frame)
quarters = Entry(frame)
dimes = Entry(frame)
nickels = Entry(frame)
pennies = Entry(frame)

#add the created coin number input boxes to the grid in the gui interface
dollars.grid(row=1,column=1)
halfDollars.grid(row=2,column=1)
quarters.grid(row=3,column=1)
dimes.grid(row=4,column=1)
nickels.grid(row=5,column=1)
pennies.grid(row=6,column=1)

#create the labels for the coin amounts
Label(frame, text = "Dollar coin amount: $").grid(row=1, column=2)
Label(frame, text = "Half Dollar amount: $").grid(row=2, column=2)
Label(frame, text = "Quarter amount: $").grid(row=3, column=2)
Label(frame, text = "Dime amount: $").grid(row=4, column=2)
Label(frame, text = "Nickel amount: $").grid(row=5, column=2)
Label(frame, text = "Pennie amount: $").grid(row=6, column=2)


#create the input boxes for the coin amounts
dollars2 = Entry(frame)
halfDollars2 = Entry(frame)
quarters2 = Entry(frame)
dimes2 = Entry(frame)
nickels2 = Entry(frame)
pennies2 = Entry(frame)

#add the created coin amount input boxes to the grid in the gui interface
dollars2.grid(row=1,column=3)
halfDollars2.grid(row=2,column=3)
quarters2.grid(row=3,column=3)
dimes2.grid(row=4,column=3)
nickels2.grid(row=5,column=3)
pennies2.grid(row=6,column=3)

#create quit button and total button and add it to the grid

Button(frame, text="Quit", command=frame.destroy).grid(row=7,column=0,sticky=W,pady=5)


Label(frame, text="Total $").grid(row=7, column=2)

total = Entry(frame)
total.grid(row=7, column=3)

#create a function to calculate the dollar amounts for the coin types and the total dollar amount
def amount():
    dollarAmount= int(dollars.get())*1
    halfDollarAmount = int(halfDollars.get())*.5
    quarterAmount = int(quarters.get())*.25
    dimeAmount = int(dimes.get())*.10
    nickelAmount = int(nickels.get())*.05    
    pennieAmount = int(pennies.get())*.01

    total_amount = dollarAmount + halfDollarAmount + quarterAmount + dimeAmount + nickelAmount + pennieAmount 

    #delete the values in the dollar amount input boxes to show the new values calculated from the coin number input boxes 
    dollars2.delete(0,END)
    dollars2.insert(0,dollarAmount)
    halfDollars2.delete(0,END)
    halfDollars2.insert(0,halfDollarAmount)
    quarters2.delete(0,END)
    quarters2.insert(0,quarterAmount)
    dimes2.delete(0,END)
    dimes2.insert(0,dimeAmount)
    nickels2.delete(0,END)
    nickels2.insert(0,nickelAmount)
    pennies2.delete(0,END)
    pennies2.insert(0,pennieAmount)
    
    total.delete(0,END)
    total.insert(0,total_amount)


Button(frame, text='Result', command=amount).grid(row=7,column=3, sticky=E,pady=5)

#function to allow only a numeric value or backspace, no negativo or decimal numbers allowed
def allow_only_numeric(e):
    #allows only numeric input
    if e.isdigit():
        return True
    #allows backspaces
    elif e=="":
        return True
    else:
        return False

#these statements will run after each keypress the allow_only_numeric function to check for and allow only numeric values 
dollars.configure(validate="key", validatecommand=(frame.register(allow_only_numeric),'%P'))
halfDollars.configure(validate="key", validatecommand=(frame.register(allow_only_numeric),'%P'))
quarters.configure(validate="key", validatecommand=(frame.register(allow_only_numeric),'%P'))
dimes.configure(validate="key", validatecommand=(frame.register(allow_only_numeric),'%P'))
nickels.configure(validate="key", validatecommand=(frame.register(allow_only_numeric),'%P'))
pennies.configure(validate="key", validatecommand=(frame.register(allow_only_numeric),'%P'))


frame.mainloop()
