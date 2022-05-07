# """ TKINTER """ #

#1st program#
from Tkinter import *
root = Tk()
a = Label(root,text='hai')
a.pack()
root.mainloop()


#2nd program#
from Tkinter import *
root = Tk()
b = Label(root,text='hello how are you')
c = Label(root,text='hello how are ')
d = Label(root,text='hello how  ')
b.pack()
d.pack()
c.pack()
root.mainloop()

#3rd program#
from Tkinter import *
root = Tk()
logo = PhotoImage(file="tt.gif")
e = Label(root, image=logo).pack(side="right")
explanation = """some message.
akshfkas;dhfkahkshdfalk
sdfjasdhf"""
f = Label(root, 
           compound=CENTER,
           fg='blue',
           bg='red', 
           text=explanation,image=logo).pack(side="left")
root.mainloop()

#4th program#
from Tkinter import *
root = Tk()
logo = PhotoImage(file="tt.gif")
explanation = """some message.
akshfkas;dhfkahkshdfalk
sdfjasdhf"""
g = Label(root, 
          compound=CENTER,
          fg='blue',
          bg='red', 
          text=explanation,image=logo).pack(side="left")
root.mainloop()

#5th program#
import Tkinter as tk
counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
root = tk.Tk()
logo = tk.PhotoImage(file="tt.gif")
root.title("Counting Seconds")
label = tk.Label(root,compound=tk.CENTER, fg="black",image=logo,font = "Helvetica 25 bold italic")
label.pack()
button1 = tk.Button(root, text='Start', width=25, command=lambda: counter_label(label))
button2 = tk.Button(root, text='Stop', width=25, command=root.destroy)
button1.pack()
button2.pack()
root.mainloop()

#6th program#
from Tkinter import *
def show_entry_fields():
	root = Tk()
	text="username: %s\npassword: %s" % (e1.get(), e2.get())
	w=Label(root,text=text)
	w.pack()
	root.mainloop()
master = Tk()
Label(master, text="Username").grid(row=0)
Label(master, text="Password").grid(row=1)
h = Entry(master)
i = Entry(master)
h.grid(row=0, column=1)
i.grid(row=1, column=1)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
mainloop( )
