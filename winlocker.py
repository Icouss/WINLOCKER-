from tkinter import * #joining library tkinter python
from tkinter import messagebox #joining library for messagebox
def btn_click():
    k = ent.get() #loops for password
    if k == "'test": #our correct password
    	messagebox.showinfo(title = '$#@$@# WIN#@#@R@#D', message = 'WINCLOKER@#&(!#@#@#@')
    	root.destroy() #if we input correct password, programm will be close by self
    else:  
        messagebox.showwarning(title = 'FUCK ALL#@#@@#', message = 'DASD#@#@!!#')
def exits():
    if ent.get() != "test":
        messagebox.showwarning(title = 'ERROR', message = 'ERRORF3SK3223')
root = Tk()
root.title('YOUR COMPUTER IS LOCKED! WINLOCKER TEST FROM DANASOFT')
root.geometry('1440x1050')
root['bg'] = 'darkred'
Label(root, text = 'ENTER PASSWORD THAT UNLOCK YOUR COMPUTER!', font = 'Arial 25', bg = 'darkred', fg = 'white').pack()
ent = Entry(root, text = '', font = 'Arial 25', width = 15)
ent.pack()
Button(root, text = 'unlock', font = 'Arial 25', bg = 'black', fg = 'white').pack()
root.mainloop()
