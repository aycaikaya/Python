import docclass
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog



import string
class SpamChecker(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.var=StringVar()
        self.var2=StringVar()
        frame1=Frame(self)
        frame2=Frame(self)
        frame3=Frame(self)

        self.main_label=Label(frame1,text='Spam Checker',font=('times',14,'bold'))
        self.upl_csv_file=Button(frame1,text='Upload Spam Training File',font=('times',12,'bold'),command=self.upload_csv_button)
        self.lb1=Label(frame1,text='Please enter the text here to check the spam',font=('times',12,'bold'))
        self.lbox=Entry(frame2)
        self.lbl2=Label(frame3,text='Threshold',font=('Times',12,'bold'))
        self.thrs=Entry(frame3)
        self.run_but=Button(frame3,text='Run Spam Checker',font=('times',12,'bold'),command=self.run_spamche_button)
        self.result_lbl=Label(frame3,textvariable=self.var)
        self.thrs.insert(0,'3')
        self.var.set('Result')


        self.main_label.pack(fill=BOTH,expand=True)
        self.upl_csv_file.pack(expand=True)
        self.lb1.pack(fill=BOTH,expand=True)
        self.lbox.pack(fill=BOTH,expand=True)
        self.lbl2.pack(expand=True,anchor=NW)
        self.thrs.pack(expand=True,anchor=NW)
        self.run_but.pack(expand=True)
        self.result_lbl.pack(fill=BOTH,expand=True)

        frame1.pack(fill=BOTH,expand=True)
        frame2.pack(fill=BOTH,expand=True)
        frame3.pack(fill=BOTH,expand=True)

    def upload_csv_button(self):
        self.file_path = tkFileDialog.askopenfilename(initialdir='/', title='Select file',
                                         filetypes=(('csv files', '*.csv'), ('all files', '*.*')))

        with open(self.file_path) as f:
            s = f.read()
        my_d=repr(s)
        docclass.getwords(my_d)
        c1 = docclass.classifier(docclass.getwords)
        docclass.sampletrain(c1)
    def run_spamche_button(self):
        c1 = docclass.naivebayes(docclass.getwords)
        docclass.sampletrain(c1)
        c1.setthreshold('bad', 3.0)
        user_input=self.lbox.get()
        if user_input=='':
            self.var.set('Please load the spam training test!')
        else:
            ans=c1.classify(user_input,default='unkown')
            if ans=='bad':
                self.var.set('spam')

            else:
                self.var.set('ham')



def main():
    root = Tk()
    g = SpamChecker(root)
    root.title('Spam Checker')
    root.geometry('530x400+420+70')
    g.pack(fill=BOTH, expand=True)
    root.mainloop()
main()
