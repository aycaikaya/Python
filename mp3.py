from tkinter import *
from tkinter.filedialog import askopenfilename
import xlrd
import pandas as pd
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import clusters1
dendogram_file_name='clusters.jpg'


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

    def cluster_distrcits_but(self):
        self.dist_listb.selection_clear(0,END)
        if self.file_path != '':
            try:
                self.data_center.cluster_dists([],threshold=int(self.combox.get()[:-1]))
                dendrogram_image = Image.open(DENDROGRAM_FILE_NAME)
                self.dendrogram_image = ImageTk.PhotoImage(dendrogram_image)
                self.canvas.create_image(0, 0, image=self.dendrogram_image, anchor='nw')
            except (ZeroDivisionError, IndexError):
                self.canvas.delete("all")
            finally:
                self.canvas.config(scrollregion=self.canvas.bbox(ALL))
                self.place_analysis_on_grid()






class Data_Center:
    def __init__(self):
        self.whole={}
        self.districts=[]
        self.parties=[]
        self.political_party_vote_percentages={}
        vote=0
    def parse_data(self,file_path):
        workbook = xlrd.open_workbook(file_path)
        worksheet = workbook.sheet_by_index(0)
        try:
            for i in range(9, 21):
                party = worksheet.cell_value(10, i)
                self.parties.append(party)
            for i in range(11,50):
                district=worksheet.cell_value(i,2)
                self.districts.append(district)
            for i in range(11,50):
                vote=worksheet.cell_value(i,9)
                vote+=vote
                self.political_party_vote_percentages['SAADET']=float((8569494/vote))*100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 10)
                vote += vote
                self.political_party_vote_percentages['BTP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 11)
                vote += vote
                self.political_party_vote_percentages['TKP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 12)
                vote += vote
                self.political_party_vote_percentages['VATAN'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 13)
                vote += vote
                self.political_party_vote_percentages['BBP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 14)
                vote += vote
                self.political_party_vote_percentages['AK PARTİ'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 15)
                vote += vote
                self.political_party_vote_percentages['CHP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 16)
                vote += vote
                self.political_party_vote_percentages['DP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 17)
                vote += vote
                self.political_party_vote_percentages['MHP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 18)
                vote += vote
                self.political_party_vote_percentages['İYİ PARTİ'] = float((8569494 / vote))* 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 19)
                vote += vote
                self.political_party_vote_percentages['HDP'] = float((8569494 / vote)) * 100.0
            for i in range(11, 50):
                vote = worksheet.cell_value(i, 20)
                vote += vote
                self.political_party_vote_percentages['DSP'] = float((8569494 / vote)) * 100.0
        except ZeroDivisionError:
            vote=0.0

        saadet = pd.read_excel(file_path, usecols=[9], skiprows=10)
        btp = pd.read_excel(file_path, usecols=[10], skiprows=10)
        tkp = pd.read_excel(file_path, usecols=[11], skiprows=10)
        vatan = pd.read_excel(file_path, usecols=[12], skiprows=10)
        bbp = pd.read_excel(file_path, usecols=[13], skiprows=10)
        chp = pd.read_excel(file_path, usecols=[14], skiprows=10)
        ak = pd.read_excel(file_path, usecols=[15], skiprows=10)
        dp = pd.read_excel(file_path, usecols=[16], skiprows=10)
        mhp = pd.read_excel(file_path, usecols=[17], skiprows=10)
        iyi = pd.read_excel(file_path, usecols=[18], skiprows=10)
        hdp = pd.read_excel(file_path, usecols=[19], skiprows=10)
        dsp = pd.read_excel(file_path, usecols=[20], skiprows=10)
        saadet_dict = saadet.to_dict()
        btp_dict = btp.to_dict()
        tkp_dict = tkp.to_dict()
        vatan_dict = vatan.to_dict()
        bbp_dict = bbp.to_dict()
        chp_dict = chp.to_dict()
        ak_dict = ak.to_dict()
        dp_dict = dp.to_dict()
        mhp_dict = mhp.to_dict()
        iyi_dict = iyi.to_dict()
        hdp_dict = hdp.to_dict()
        dsp_dict = dsp.to_dict()
        self.whole = (
        saadet_dict, btp_dict, tkp_dict, vatan_dict, bbp_dict, chp_dict, ak_dict, dp_dict, mhp_dict, iyi_dict, hdp_dict,
        dsp_dict)

    def cluster_dists(self,selected_districts, threshold=0):
        assert self.whole != {}
        if not selected_districts:
            selected_districts = self.districts
        political_party_names=[political_party for political_party in self.parties
                               if self.political_party_vote_percentages[political_party] >= threshold]
        cluster_matrix = [[0.0] * len(political_party_names) for i in range(len(selected_districts))]
        for i in range(len(selected_districts)):
            for j in range(len(political_party_names)):
                cluster_matrix[i][j] = self.districts[selected_districts[i]] \
                    .get_political_party_percentage(political_party_names[j]),

        cluster = hcluster(cluster_matrix, distance=sim_distance)
        drawdendrogram(cluster, selected_districts)







def main():
    data_center=Data_Center()
    g=PoliCluster(data_center)
    g.interface()
main()




#di['CHP']['Adalar']=43






