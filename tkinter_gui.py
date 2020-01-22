import tkinter as tk
import string
import random

#future improvements that I can do once I've gained more skills -- better syntax that I can only partially understand logically for now

#function -- the print function for each password type could be integrted within the password generator function
#a loop could be written for varying the range of which the string is defined
def pw_weak(chars = string.ascii_letters+string.digits+string.punctuation):
    return ''.join([random.choice(chars) for n in range(5)])

def pw_medium(chars = string.ascii_letters+string.digits+string.punctuation):
    return ''.join([random.choice(chars) for n in range(10)])

def pw_strong(chars = string.ascii_letters+string.digits+string.punctuation):
    return ''.join([random.choice(chars) for n in range(15)])

weak = pw_weak()
medium = pw_medium()
strong = pw_strong()

def show_weak():
    print(weak)

def show_medium():
    print(medium)

def show_strong():
    print(strong)

# the generator only allows for printing in the console instead of another GUI element
root = tk.Tk()
root.title('PASSWORD GENERATOR')
root.geometry('300x300')

label = tk.Label(root, text='Generate Password')
label.pack()

button1 = tk.Button(root, text='Weak', command=show_weak)
button1.pack()

button2 = tk.Button(root, text='Medium', command=show_medium)
button2.pack()

button3 = tk.Button(root, text='Strong', command=show_strong)
button3.pack()

#class: Popup
    #def __init__:
    #these all ask for self to be passed through


root.mainloop()