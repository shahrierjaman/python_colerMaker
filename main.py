from tkinter import *
from tkinter.constants import *
#this is a cooment
class colormaker:
    def __init__(self,root):
        self.root = root
        self.root.title("My color maker")
        self.root.geometry("300x420")
        self.root.configure(bg="#b1b3b5")
        self.root.resizable(0,0)
        self.hex =""
        self.color_frame = Label(self.root,bg="#000000",width=40,height=10,bd=1,relief=RAISED)
        #self.color_frame.bind("<Double-1>",self.copy_color)
        self.color_frame.place(x=7,y=7)

        frame = Frame(self.root,bd=2,relief=SUNKEN)
        frame.place(x=7,y=170,width=285,height=170)


        r_label = Label(frame,text="R",font="arial 10 bold",fg="#ff0000")
        r_label.place(x=5,y=20)
        self.r_scale = Scale(frame,from_=0,to=255,length=210,fg="#ff0000",orient=HORIZONTAL,command=self.scaleController)
        self.r_scale.set(0)
        self.r_scale.place(x=40,y=0)

        g_label = Label(frame, text="G", font="arial 10 bold", fg="green")
        g_label.place(x=5, y=68)
        self.g_scale = Scale(frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL,command=self.scaleController)
        self.g_scale.set(0)
        self.g_scale.place(x=40, y=50)

        b_label = Label(frame, text="B", font="arial 10 bold", fg="blue")
        b_label.place(x=5, y=122)
        self.b_scale = Scale(frame, from_=0, to=255, length=210, fg="blue", orient=HORIZONTAL,command=self.scaleController)
        self.b_scale.set(0)
        self.b_scale.place(x=40, y=105)

        hex_label = Label(self.root,text="Hex code",font="arial 10 bold",bg="#b1b3b5")
        hex_label.place(x=7,y=360)

        self.hex_entry = Entry(self.root,width=12,font="arial 10")
        self.hex_entry.insert(0,"#000000")
        self.hex_entry.place(x=80,y=361)

        rgb_label = Label(self.root, text="RGB code", font="arial 10 bold", bg="#b1b3b5")
        rgb_label.place(x=7, y=390)

        self.rgb_entry = Entry(self.root, width=12, font="arial 10")
        self.rgb_entry.insert(0,"0,0,0")
        self.rgb_entry.place(x=80, y=391)


    def scaleController(self,*arg):
        r = int(self.r_scale.get())
        g = int(self.g_scale.get())
        b = int(self.b_scale.get())

        self.hex = "#%02x%02x%02x"%(r,g,b)
        self.color_frame.config(bg=self.hex)

        self.hex_entry.delete(0,END)
        self.hex_entry.insert(0,self.hex)

        rgb = f"{r},{g},{b}"
        self.rgb_entry.delete(0, END)
        self.rgb_entry.insert(0, rgb)

    #def copy_color(self):
        #self.root.clipboard_clear()
        #self.root.clipboard_append(self.hex)




root = Tk()
cm = colormaker(root)
root.mainloop()
