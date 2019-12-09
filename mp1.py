from tkinter import *
from tkinter.ttk import *
from functools import *


class SteelBoxInc(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()


    def initUI(self):

        self.screenvar1=StringVar()
        self.screenvar2=StringVar()
        self.screenstr1=''
        self.screenstr2=''
        self.price=StringVar()
        self.price.set('0')

        self.exrate=StringVar()
        self.exrate.set('0')

        self.widthvar=StringVar()
        self.widthvar.set('0')

        self.lengthvar=StringVar()
        self.lengthvar.set('0')

        self.heightvar=StringVar()
        self.heightvar.set('0')

        self.thicknessvar=StringVar()
        self.thicknessvar.set('0')

        self.var1=IntVar()
        self.var2=IntVar()

        self.main_label = Label(self, text='SteelBox Inc. Calculator', font=('Times', 15, 'bold'))

        self.importb = Button(self, text='Import')

        self.L1=Label(self,text='Width',font=('Times',10))
        self.L2 = Label(self, text='Length', font=('Times', 10))
        self.L3 = Label(self, text='Height', font=('Times', 10))
        self.L4 = Label(self, text='Thickness', font=('Times', 10))


        self.width=Entry(self,textvariable=self.widthvar)
        self.length=Entry(self,textvariable=self.lengthvar)
        self.height=Entry(self,textvariable=self.heightvar)
        self.thickness=Entry(self,textvariable=self.thicknessvar)

        self.L7 = Label(self, text='Total Weight', font=('Times', 10))
        self.totalW = Label(self,textvariable=self.screenvar2)


        self.L8 = Label(self, text='Total Price', font=('Times', 10))
        self.totalP = Label(self,textvariable=self.screenvar1)


        self.c1=Checkbutton(self,text='Lid?',variable=self.var1)
        self.c2=Checkbutton(self,text='Seperator?',variable=self.var2)

        self.L5=Label(self,text='Current Steel Price',font=('Times',10))
        self.CurStP=Entry(self,textvariable=self.price)

        self.L6=Label(self,text='TRY/USD Exchange Rate',font=('Times',10))
        self.bex=Entry(self,textvariable=self.exrate)

        self.getbb = Button(self, text='Get')

        self.clc=Button(self, text='Calculate',command=self.calculate)

        self.exportb=Button(self, text='Export')

        self.layoutGrid()
        self.pack()

    def layoutGrid(self):
        self.columnconfigure(0,pad=3)
        self.columnconfigure(1,pad=3)
        self.columnconfigure(2,pad=3)
        self.columnconfigure(3,pad=3)
        self.columnconfigure(4,pad=3)
        self.columnconfigure(5,pad=3)
        self.columnconfigure(6,pad=3)



        self.rowconfigure(0,pad=3)
        self.rowconfigure(1,pad=3)
        self.rowconfigure(2,pad=3)
        self.rowconfigure(3,pad=3)
        self.rowconfigure(4,pad=3)
        self.rowconfigure(5,pad=3)
        self.rowconfigure(6,pad=3)
        self.rowconfigure(7,pad=3)

        self.main_label.grid(in_=self,row=0,column=3)
        self.importb.grid(in_=self,row=1,column=1)
        self.L1.grid(in_=self,row=2,column=1)
        self.L2.grid(in_=self,row=3,column=1)
        self.L3.grid(in_=self,row=4,column=1)
        self.L4.grid(in_=self,row=5,column=1)
        self.clc.grid(in_=self,row=6,column=1)
        self.width.grid(in_=self,row=2,column=2)
        self.length.grid(in_=self,row=3,column=2)
        self.height.grid(in_=self,row=4,column=2)
        self.thickness.grid(in_=self,row=5,column=2)
        self.c1.grid(in_=self,row=2,column=3)
        self.c2.grid(in_=self,row=2,column=4)
        self.L5.grid(in_=self,row=4,column=3)
        self.CurStP.grid(in_=self,row=4,column=4)
        self.L6.grid(in_=self,row=5,column=3)
        self.bex.grid(in_=self,row=5,column=4)
        self.getbb.grid(in_=self,row=5,column=6)
        self.clc.grid(in_=self,row=7,column=2)
        self.L7.grid(in_=self,row=6,column=3)
        self.L8.grid(in_=self,row=6,column=4)
        self.totalW.grid(in_=self,row=7,column=3,sticky=W+E)
        self.totalP.grid(in_=self,row=7,column=4,sticky=W+E)
        self.exportb.grid(in_=self,row=7,column=5)

    def calculate(self):
        weight=0
        cost=0
        density=7.85
        ent_price=float(self.CurStP.get())
        ent_exRate=float(self.bex.get())
        ent_width=float(self.width.get())
        ent_length=float(self.length.get())
        ent_height=float(self.height.get())
        ent_thick=float(self.thickness.get())
        if ent_length >= ent_width:
            surface_area=2*((ent_width*ent_length)+(ent_width*ent_height))
            volume=surface_area*ent_thick
            weight=volume*density
            cost=ent_price*weight*ent_exRate
        elif ent_length < ent_width:
            new_length=ent_width
            new_width=ent_length
            surface_area=2*(new_width*new_length)+(new_width*new_length)
            volume=surface_area*ent_thick
            weight=volume*density
            cost=ent_price*weight
        self.screenstr1 = str(cost)
        self.screenstr2 = str(weight)
        self.screenvar1.set(self.screenstr1)
        self.screenvar2.set(self.screenstr2)
        return

    #def imp(self):
        #sample_input=anydbm.open('sample_input.db',w)








def main():
    root=Tk()
    root.title('SteelBoxInc')
    root.geometry('730x500+420+150')
    my_app=SteelBoxInc(root)
    root.mainloop()
main()
if __name__ == '__main__':
    main()