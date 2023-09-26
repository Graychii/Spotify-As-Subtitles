from tkinter import *
from PIL import Image, ImageTk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)
def RBGAImage(path):
    return Image.open(path).convert("RGBA")
root = Tk()
wdth = int(root.winfo_screenwidth() )
wdwdwd = root.winfo_screenwidth()
root.wm_attributes("-topmost", 1)
root.geometry(f"{wdwdwd}x50+{str(0)}+980")
root.config(bg = 'grey')
root.wm_attributes('-transparentcolor','grey')
root.attributes('-alpha', 0.7)


def getlyrics():
	return open('lyrics.txt').read() 

# you are working with

lab = Label(root,font=("Helvetica", 25),foreground = 'white')
lab.config(borderwidth=0)
lab['text'] = getlyrics()
lab.configure(bg="black")

root.bind('<Escape>', lambda e, w=root: w.destroy())
lab.pack()
def update():
	lab['text'] = getlyrics()


	root.after(50, update) 


update()


# setting window over others     
root.overrideredirect(True)
root.mainloop()


