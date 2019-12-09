from tkinter import *
from tkinter.filedialog import askopenfilename
import xlrd
import pandas as pd
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import clusters
dendogram_file_name='clusters.jpg'

class District:
    def __init__(self,name):
        self.name=name
        self.election_result={}#key=political party acronym/value=vote percentage in that district
    def add_election_result(self,party_acronym,district_name,vote_percentage):
        self.election_result[party_acronym][district_name]=vote_percentage
class PoliticalParty:
    def __init__(self,acronym):
        self.acronym=acronym
        self.election_results={}
    def add_election_result(self,district_name,party_acronym,vote_percentage):
        self.election_results[district_name][party_acronym]=[vote_percentage]

class DataCenter:
    def __init__(self):
        self.district_names=[]
        self.party_acronyms=[]
        self.v





class PoliCluster:
    def __init__(self,data_center):
        self.data_center=data_center
        self.root=Tk()
        self.frame1=None
        self.frame2=None
        self.Frame3=None
        self.canvas=None
        self.initUI()

    def interface(self):
        self.root.title('Clustering')
        self.root.geometry('730x600+420+70')
        self.root.deiconify()
        Tk.mainloop(self.root)

    def initUI(self):
        self.frame1=Frame(self.root)
        self.frame2=Frame(self.root)
        self.frame3=Frame(self.root)

        self.frame1.pack(fill=BOTH)
        self.main_label = Label(self.frame1, text='Election Data Analysis Tool v.1.0', bg='red', fg='white',font=('Times', 14, 'bold'))
        self.loadDataB = Button(self.frame1, text='Load Election Data', height=2, width=27,command=self.load_data_button)
        self.clusDisB = Button(self.frame1, text='Cluster Districts', height=4, width=16,command=self.cluster_distrcits_but)
        self.clusPolB = Button(self.frame1, text='Cluster Political Parties', height=4, width=18)


        self.frame2.pack(expand=True,fill=BOTH)
        self.x_scroll=Scrollbar(self.frame2,orient=HORIZONTAL)
        self.y_scroll=Scrollbar(self.frame2,orient=VERTICAL)
        self.canvas=Canvas(self.frame2,xscrollcommand=self.x_scroll.set,yscrollcommand=self.y_scroll.set)


        self.frame3.pack(expand=True)
        self.dist_lab=Label(self.frame3,text='Districts')
        self.dist_scroll=Scrollbar(self.frame3)
        self.dist_listb=Listbox(self.frame3,yscrollcommand=self.dist_scroll.set,height=10,selectmode=EXTENDED)
        self.combox_label=Label(self.frame3,text='Threshold')
        self.combox = Combobox(self.frame3,values=['0%', '1%', '10%', '20%', '30%', '40%', '50%'], width=6, state="readonly")
        self.refine_but=Button(self.frame3,text='Refine Analysis')


        self.main_label.pack(fill=X, expand=True, anchor=N)
        self.loadDataB.pack(expand=True, anchor=N)
        self.clusDisB.pack(side=LEFT, expand=True, anchor=NE)
        self.clusPolB.pack(side=LEFT, expand=True, anchor=NW)
        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.canvas.pack(fill=BOTH, expand=True)

        self.x_scroll.configure(command=self.canvas.xview)
        self.y_scroll.configure(command=self.canvas.yview)

        self.dist_lab.pack(side=LEFT)
        self.dist_listb.pack(side=LEFT)
        self.dist_scroll.pack(side=LEFT,fill=Y)
        self.dist_scroll.configure(command=self.dist_listb.yview)

        self.combox_label.pack(side=LEFT)
        self.combox.pack(side=LEFT)
        self.combox.current(0)
        self.refine_but.pack(side=LEFT)


    def load_data_button(self):
        self.file_path = askopenfilename(initialdir='/', title='Select file',filetypes=(('excel files', '*.xlsx'), ('all files', '*.*')))
        if self.file_path != '':
            self.data_center.parse_data(self.file_path)
            for name in self.data_center.districts:
                self.dist_listb.insert(END, name)






















def main():
    data_center=Data_Center()
    g=PoliCluster(data_center)
    g.interface()
main()