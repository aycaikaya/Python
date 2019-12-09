from tkinter import *
from tkinter.filedialog import askopenfilename
import xlrd

class PoliCluster(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.main_label = Label(self, text='Election Data Analysis Tool v.1.0', bg='red', fg='white',
                                font=('Times', 14, 'bold'))

        self.loadDataB = Button(self, text='Load Election Data', height=2, width=27, command=self.askFile)

        self.clusDisB = Button(self, text='Cluster Districts', height=4, width=16)

        self.clusPolB = Button(self, text='Cluster Political Parties', height=4, width=18)

        self.main_label.pack(fill=X, expand=True, anchor=N)
        self.loadDataB.pack(expand=True, anchor=N)
        self.clusDisB.pack(side=LEFT, expand=True, anchor=NE)
        self.clusPolB.pack(side=LEFT, expand=True, anchor=NW)


        self.pack()

    #tkfiledilaog method
    def askFile(self):
        self.ex_file_path=askopenfilename()
        return self.ex_file_path


    #reading the data as a list of political party names
    def loadParties(self,data):
        workbook = xlrd.open_workbook(data)
        worksheet = workbook.sheet_by_index(0)
        parts=[]
        for i in range(9, 21):
            party = worksheet.cell_value(10, i)
            parts.append(party)
        return parts

    #reading the data as list of districts
    def loadDistricts(self,data):
        workbook=xlrd.open_workbook(data)
        worksheet=workbook.sheet_by_index(0)
        dists=[]
        for i in range(11,50):
            district=worksheet.cell_value(i,2)
            dists.append(district)
        return dists

    #the dictionary that is needed for clustering parties
    #key: political party acronym, value: vote percentage in that district
    def clusterParties(self):
        self.path=self.askFile
        partylist=self.loadParties(self.path)
        distlist=self.loadDistricts(self.path)










def main():
    root = Tk()
    root.geometry('730x500+420+150')
    root.title('Clustering')
    p = PoliCluster(root)
    p.pack(fill=BOTH)
    root.mainloop()


main()