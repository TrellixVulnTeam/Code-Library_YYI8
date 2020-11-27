from tkinter import *


root = Tk()
root.title('Spin Box')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x400')

def grab():
    my_label.config(text=my_spin.get())

# my_spin = Spinbox(root, from_=0, to=10, increment=2, font=('Helvetica', 20))
my_spin = Spinbox(root, values=('John', 'Tim', 'Bob'), font=('Helvetica', 20))
my_spin.pack(pady=20)

my_button = Button(root, text='Submit', command=grab)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
