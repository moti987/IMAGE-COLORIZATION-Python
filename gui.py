from tkinter import *
from tkinter import filedialog
from tkinter import ttk
filepath=''
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "C:/Users",
                                          title = "Select a File",
                                          filetypes = [("all files","*.*")])
    global filepath
    filepath=filename
    print(filepath)
def imgselect():
    root = Tk()
    frm = ttk.Frame(root,padding=10)
    frm.grid()
    ttk.Label(frm,text="Please browse and select an image").grid(column=0,row=0)
    ttk.Button(frm,text="Browse",command=browseFiles).grid(column=0,row=1)
    ttk.Button(frm,text="confirm",command=root.destroy).grid(column=0,row=2)
    root.mainloop()
    return(filepath)