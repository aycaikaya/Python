# from tkinter import *
#
# root=Tk()


# master = Tk()
# label1 = Label(master, text="First")
# label2 = Label(master, text="Second")
# entry1 = Entry(master)
# entry2 = Entry(master)
# checkbutton = Checkbutton(master, text="Show title")
# label3 = Label(master, text='Hello!' )
# ok_button = Button(master, text="OK")
# cancel_button = Button(master, text="Cancel")
#
# label1.grid(sticky=E) # by default column 0 of the next empty row
# label2.grid(sticky=E) # can you guess row and column number of this guy?
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# checkbutton.grid(columnspan=2, sticky=W)
# label3.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
# ok_button.grid(row=2, column=2)
# cancel_button.grid(row=2, column=3)
# master.mainloop()

# button1=Button(root,text='Istanbul')
# frame=Frame(root)
# button2=Button(root,text='Sehir')
# button3=Button(root,text='University')


# button1.pack(fill=BOTH,expand=True)
# frame.pack(expand=True,fill=BOTH)
# button2.pack(side=LEFT,expand=True,fill=BOTH)
# button3.pack(side=LEFT,expand=True,fill=BOTH)
# root.mainloop()


# Grid.rowconfigure(root,0,weight=1)
# Grid.rowconfigure(root,1,weight=1)
# Grid.columnconfigure(root,0,weight=1)
# Grid.columnconfigure(root,1,weight=1)

# button1.grid(row=0,column=0,columnspan=2,sticky=N+E+W+S)
# button2.grid(row=1,column=0,sticky=N+E+S+W)
# button3.grid(row=1,column=1,sticky=N+E+S+W)
# button1.grid(row=0,column=0,sticky=N+E+S+W)
# button2.grid(row=0,column=1,sticky=N+E+W+S)
# button3.grid(row=1,column=0,columnspan=2,sticky=N+E+W+S)
#
# root.mainloop()


# while True:
#     try:
#          val=input('Enter an integer: ')
#          intval=int(val)
#          break
#     except ValueError:
#         print('oops')
# print('finished')



# class Professor:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         self.research_areas=[]
#     def add_reasearch_areas(self,research_area):
#         self.research_areas.append(research_area)
#
#
# class Department:
#     def __init__(self,name,website):
#         self.name=name
#         self.website=website
#         self.professors={}
#     def add_proffessor(self,professor):
#         self.professors[professor.name]=professor
#     def print_infor(self):
#         print('Name:',self.name)
#         print('Website:',self.website)
#         print('Professors:')
#         for i in self.professors:
#             professor=self.professors[i]
#             print('',professor.name,str(professor.salary),professor.research_areas)
# ayse=Professor('Ayse',1000)
# ahmet=Professor('Ahmet',800)
# ayse.add_reasearch_areas('Machine Learning')
# ahmet.add_reasearch_areas('Bioinformatics')
#
# dept=Department('Computer Science','Link')
# dept.add_proffessor(ayse)
# dept.add_proffessor(ahmet)
# dept.print_infor()


# class Midstudy(Frame):
#     def __init__(self,parent):
#         Frame.__init__(self,parent)
#         self.parent=parent
#         self.initUI()
#     def initUI(self):
#         self.var=BooleanVar()
#         self.var2=StringVar()
#         cities=['Paris','Rome','London']
#
#
#
#         self.main_label=Label(self,text='Midterm 1 Study',font=('Times',10,'bold'))
#         self.hi_there=Button(self,text='Hello',command=self.hi)
#         self.check=Checkbutton(self,text='Show Label',textvariable=self.var,command=self.onSelf)
#         self.L2=Label(self,textvariable=self.var2)
#         self.var2.set('Another way of putting labels')
#         self.lb=Listbox(self, selectmode='Multiple')
#         for i in cities:
#             self.lb.insert(END,i)
#         self.en=Entry(self)
#
#         self.w=Label(self,text='Red',bg='red',fg='white')
#         self.a=Label(self,text='Green',bg='green',fg='black')
#         self.r=Label(self,text='Blue',bg='blue',fg='white')
#         # frame 1
#         frame1 = Frame(self, borderwidth=2, relief=GROOVE)
#         frame1.pack(side=LEFT, padx=30, pady=30)
#         # frame 2
#         frame2 = Frame(self, borderwidth=2, relief=GROOVE)
#         frame2.pack(side=LEFT, padx=10, pady=10)
#         # frame 3
#         frame3 = Frame(self, borderwidth=2, relief=GROOVE)
#         frame3.pack(side=LEFT, padx=5, pady=5)
#         # Pack the labels
#         Label(frame1, text="Frame 1").pack(padx=10, pady=10)
#         Label(frame2, text="Frame 2").pack(padx=10, pady=10)
#         Label(frame3, text="Frame 3").pack(padx=10, pady=10)
#
#
#
#
#
#
#
#
#
#         # self.check.pack()
#         # self.hi_there.pack()
#         # self.main_label.pack()
#         # self.L2.pack()
#         # self.lb.pack()
#         # self.en.pack()
#
#         self.pack()
#
#
#     def hi(self):
#         print('Hello bitch!')
#     def onSelf(self):
#         if self.var.get()==True:
#             self.parent.title('Midterm study')
#         else:
#             self.parent.title("")
#
#
#
#
#
#
#
# def main():
#     root=Tk()
#     root.title('Midterm Study')
#     root.geometry('400x400+500+200')
#     g=Midstudy(root)
#     root.mainloop()
# main()
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""
soup=BeautifulSoup(html_doc,features="html.parser")
#print(soup.tagStack)
#print(soup.p)
#print(soup.p['class'])
#print(soup.find('a'))
#print(soup.a['class'])
#print(soup.find('b'))
#print(soup.b)

def read_sales_dat(file_name):
    stores={}
    with open(file_name) as f:
        for line in f:
            line=line.strip()
            store_name,data,sale=line.split(' - ')
            stores.setdefault(store_name,{})
            stores[store_name][data]=sale
    return stores
#print(read_sales_dat(r'C:\Users\aycakaya\Desktop\midtermstud.txt'))

def get_total_state(stores,store_name):
    if store_name in stores:
        sales=stores[store_name].values()
        sale_amounts=[]
        for sale in sales:
            sale_amount,currency=sale.split(' ')
            sale_amounts.append(float(sale_amount))
        total_sale=sum(sale_amounts)
        return total_sale
    else:
        print('error')
        return 0.0
stores=read_sales_dat(r'C:\Users\aycakaya\Desktop\midtermstud.txt')
bostanci_sales=get_total_state(stores,'Bostanci')
#print(bostanci_sales)





class Sale:
    def __init__(self,store_name,date,amount):
        self.store_name=store_name
        self.date=date
        self.amount=amount
    def display(self):
        print(self.store_name+' - '+self.date+' -> '+str(self.amount)+' TRY ')
bostanci=Sale('bostanci','06.07.2019',10000)
#bostanci.display()

from tkinter import *
root=Tk()
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)

button1=Button(frame1,text='I')
button2=Button(frame2,text='will')
button3=Button(frame2,text='ace')
button4=Button(frame3,text='ENG-102!')

button1.pack(fill=BOTH,expand=True)
button2.pack(fill=BOTH,expand=True)
button3.pack(fill=BOTH,expand=True)
button4.pack(fill=BOTH,expand=True)

frame1.pack(side=LEFT,fill=BOTH,expand=True)
frame2.pack(side=LEFT,fill=BOTH,expand=True)
frame3.pack(side=LEFT,fill=BOTH,expand=True)

#root.mainloop()

line='izelisko e'
print(line)
print(line.strip('e'))