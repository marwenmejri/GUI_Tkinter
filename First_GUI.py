from tkinter import *

main_window = Tk()

## Labels
# Label(main_window, text='Hello World').pack()
# Label(main_window, text='This is Tkinter').pack()
Label(main_window, text='Enter your name').grid(row=0, column=0)
Label(main_window, text="What's your age?").grid(row=1, column=0)

## Text Input
my_name = Entry(main_window, width=50, borderwidth=5)
my_name.grid(row=0, column=1)
my_age = Entry(main_window, width=50, borderwidth=5)
my_age.grid(row=1, column=1)

def onclick():
    print(f"My name is : {my_name.get()} , My age is : {my_age.get()}")


## Buttons
Button(main_window, text='Click me', command = onclick ).grid(row=2, column=1)


main_window.mainloop()



