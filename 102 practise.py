from tkinter import *
import random

class FirstGame(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.vara=BooleanVar()
        self.varb=BooleanVar()
        self.varc=BooleanVar()
        self.var1=StringVar()
        self.var2=StringVar()
        self.var3=StringVar()
        self.c1=Checkbutton(self,text='Fast',variable=self.vara).pack()
        self.c2=Checkbutton(self, text='Normal',variable=self.varb).pack()
        self.c3=Checkbutton(self,text='Slow',variable=self.varc).pack()

        self.b1=Button(self,text='START',command=self.start).pack()
        self.b2=Button(self,text='STOP').pack()

        self.b3=Button(self,text='Your Color').pack()
        self.b4=Button(self,text='Score').pack()

        self.b5=Button(self,text=var1).pack()
        self.b6=Button(self,text=var2).pack()
        self.b7=Button(self,text=var3).pack()
        self.pack()
    def start(self):
        self.colors=['red','blue','green']
        self.selectedC=random.choice(self.colors)
        self.b3.configure(bg=self.selectedC)
        return




def main():
    root=Tk()
    root.title('First Game')
    root.geometry('400x400+500+200')
    g=FirstGame(root)
    root.mainloop()
main()

