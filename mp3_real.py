from tkinter import *
import xlrd
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk
import pandas as pd
from clusters import *

dendogram_file='clusters.jpg'
district_but=0
parties_but=1


class PCluster:
    def __init__(self,data_center):
        #keeping this varibale so that when refine analysis button pressed it will know which one(political party or district) will be clustered
        self.last_pressed_but=0
        self.data_center=data_center
        self.root=Tk()
        #declaring the frames which include canvas and the listbox part
        self.frame2=None
        self.frame3=None

        self.district_listb=None
        self.canv=None
        self.dendogram_img=None
        self.thrs_com=None
        self.initUI()
    def interface(self):
        self.root.title('Clustering')
        self.root.geometry('730x600+420+70')
        self.root.deiconify()
        Tk.mainloop(self.root)
    def initUI(self):
        frame1=Frame(self.root)
        self.frame2=frame2=Frame(self.root)
        self.frame3=frame3=Frame(self.root)

        #FRAME 1
        frame1.pack(fill=BOTH)
        self.main_label = Label(frame1, text='Election Data Analysis Tool v.1.0', bg='red', fg='white',font=('Times', 14, 'bold'))
        self.loadDataB = Button(frame1, text='Load Election Data', height=2, width=27,command=self.load_data_button)
        self.clusDisB = Button(frame1, text='Cluster Districts', height=4, width=16,command=self.cluster_districts_button)
        self.clusPolB = Button(frame1, text='Cluster Political Parties', height=4, width=18,command=self.cluster_parties_button)


        #FRAME 2
        self.x_scroll = Scrollbar(frame2, orient=HORIZONTAL)
        self.y_scroll = Scrollbar(frame2, orient=VERTICAL)
        self.canvas = Canvas(frame2, xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)


        #FRAME 3
        self.dist_lab = Label(frame3, text='Districts')
        self.dist_scroll = Scrollbar(frame3)
        self.dist_listb = Listbox(frame3, yscrollcommand=self.dist_scroll.set, height=10, selectmode=EXTENDED)
        self.combox_label = Label(frame3, text='Threshold')
        self.combox = Combobox(frame3, values=['0%', '1%', '10%', '20%', '30%', '40%', '50%'], width=6,state="readonly")
        self.refine_but = Button(frame3, text='Refine Analysis',command=self.refine_analysis_button)

        #PACKIG
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
        self.dist_scroll.pack(side=LEFT, fill=Y)
        self.dist_scroll.configure(command=self.dist_listb.yview)

        self.combox_label.pack(side=LEFT)
        self.combox.pack(side=LEFT)
        self.combox.current(0)
        self.refine_but.pack(side=LEFT)

        self.thrs_com=self.combox
        self.canv=self.canvas



    def load_data_button(self):
        self.file_path = askopenfilename(initialdir='/', title='Select file',filetypes=(('excel files', '*.xlsx'), ('all files', '*.*')))
        if self.file_path != '':
            self.data_center.parse_data(self.file_path)
            for name in self.data_center.district_names:
                self.dist_listb.insert(END, name)


    def cluster_districts_button(self):
        self.last_pressed_but=district_but
        self.dist_listb.selection_clear(0,END)
        try:
            self.data_center.cluster_districts([], threshold=int(self.thrs_com.get()[:-1]))
            dendrogram_image = Image.open(dendogram_file)
            self.dendrogram_img = ImageTk.PhotoImage(dendrogram_image)
            self.canvas.create_image(0, 0, image=self.dendrogram_img, anchor='nw')
        except (ZeroDivisionError,IndexError):
            self.canvas.delete('all')
        finally:
            self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
            self.pack_other_frames()
    def cluster_parties_button(self):
        self.last_pressed_but=parties_but
        self.dist_listb.selection_clear(0,END)
        try:
            self.data_center.cluster_political_parties([],threshold=int(self.thrs_com.get()[:-1]))
            dendrogram_image=Image.open(dendogram_file)
            self.dendogram_img=ImageTk.PhotoImage(dendrogram_image)
            self.canvas.create_image(0,0,image=self.dendogram_img,anchor='nw')
        except (ZeroDivisionError,IndexError):
            self.canvas.delete('all')
        finally:
            self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
            self.pack_other_frames()

    def refine_analysis_button(self):
        selected_districts=[self.data_center.political_party_names[index] for index in self.dist_listb.curselection()]
        try:
            if self.last_pressed_but==district_but:
               self.data_center.cluster_districts(selected_districts,int(self.thrs_com.get()[:-1]))
            else:
                self.data_center.cluster_political_parties(selected_districts,int(self.thrs_com.get()[:-1]))
            dendogram_img=Image.open(dendogram_file)
            self.dendogram_img=ImageTk.PhotoImage(dendogram_img)
            self.canvas.create_image(0, 0, image=self.dendogram_img, anchor='nw')
        except(ZeroDivisionError,IndexError,KeyError):
            self.canvas.delete('all')

        finally:
            self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
            self.pack_other_frames()









    def pack_other_frames(self):
        self.frame2.pack(expand=True,fill=BOTH)
        self.frame3.pack(expand=True)

class DataCenter:
    # Constructor
    def __init__(self):
        # Declare instance variabless
        self.dist_percentage_per_poli={'ADALAR':{'SAADET':0.4309912799438709,'BTP':0.07016137115365341,
                                                 'TKP':0.21732516190724563,'VATAN PARTISI':0.2906685376365641,'BBP':0.0,
                                                 'CHP':44.10143329658214,'AK PARTI':30.74070361832214,'DP':0.0,
                                                 'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':24.366041896361633},

                                  'ARNAVUTKOY':{'SAADET':2.8034945886034683,'BTP':0.8758204024861999,
                                                'TKP':0.21732516190724563,'VATAN PARTISI':0.1521276133350719,
                                                'BBP':1.164138450616479,'CHP':0.0,'AK PARTI':57.7324292606598,
                                                'DP':0.3325074977180858,'MHP':0.0,'IYI PARTI':19.150693267266483,
                                                'HDP':13.729879312093422, 'DSP':0.6657394126425291},

                                  'ATASEHIR':{'SAADET':1.621149571292474,'BTP':0.16910130200063514,
                                              'TKP':0.6093204191806922,'VATAN PARTISI':0.28739282311845027,'BBP':0.0,
                                              'CHP':51.35876468720228,'AK PARTI':45.14250555731979,
                                              'DP':0.15123848840901874,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,
                                              'DSP':0.5251667195935218},

                                  'AVCILAR': {'SAADET': 0.7434423358265851, 'BTP': 0.11909913251323895,
                                              'TKP': 0.0, 'VATAN PARTISI': 0.12692917928746575, 'BBP': 0.3770785683377635,
                                              'CHP': 52.126269806927525,'AK PARTI': 45.47402691063444,
                                              'DP': 0.17267313675794854, 'MHP': 0.0, 'IYI PARTI':0.0, 'HDP':0.0,
                                              'DSP': 0.7982526632461726},
                                  'BAGCILAR':{'SAADET':3.8421486582232522,'BTP':0.32249036184981883,
                                              'TKP':0.5481873272379333,'VATAN PARTISI':0.21179976853311008,
                                              'BBP':2.364340987541635,'CHP':0.0,'AK PARTI':57.890171734312325,
                                              'DP':0.3393839148161502,'MHP':0.0,'IYI PARTI':20.492384033323162,
                                              'HDP':12.806826003968725,'DSP':1.2539050582323292},

                                  'BAHCELIEVLER':{'SAADET':1.7867766161095568,'BTP':0.2647621852451774,
                                                  'TKP':0.3635896026485057,'VATAN PARTISI':0.1493152702105728,
                                                  'BBP':1.1488735090561035, 'CHP':45.22986305404211,
                                                  'AK PARTI':49.893977322927405,'DP':1.1883375055220144,
                                                  'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':0.33809453688705643},

                                  'BAKIRKOY':{'SAADET':0.8340947272244982,'BTP':0.14810339237820153,
                                              'TKP':0.0,'VATAN PARTISI':0.0,'BBP':0.0,'CHP':56.9741224321377,
                                              'AK PARTI':24.846738778036485,'DP':0.3802057237171741,'MHP':0.0,
                                              'IYI PARTI':9.270830263196675,'HDP':0.0,'DSP':6.632968846709304},

                                  'BASAKSEHIR':{'SAADET':3.282132620975596,'BTP':0.24023522646112178,
                                                'TKP':0.5784137463526777,'VATAN PARTISI':0.1535093821595199,
                                                'BBP':1.0541595941044977,'CHP':36.752279452003975,
                                                'AK PARTI':54.75229800298671,'DP':0.0,'MHP':0.0,'IYI PARTI':0.0,
                                                'HDP':3.3976124885215793,
                                                'DSP':0.28290248675923607},


                                  'BAYRAMPASA':{'SAADET':8.36294803688099,'BTP':0.27355437503816327,'TKP':0.0,
                                                'VATAN PARTISI':0.15509556084753007,'BBP':1.189473041460585,
                                                'CHP':44.573487207669295,'AK PARTI':49.288025889967635,'DP':0.0,
                                                'MHP':0.0,'IYI PARTI':0.0,'HDP':0.7956280148989436,
                                                'DSP':0.5745863100689992},


                                  'BESIKTAS':{'SAADET':0.7590475760177111,'BTP':0.10933899606921792,
                                              'TKP':0.0,'VATAN PARTISI':0.37229476347535356,'BBP':0.28283558487326615,
                                              'CHP':73.06284733203813,'AK PARTI':0.0,'DP':0.2277142728053133,
                                              'MHP':16.3186192563141,'IYI PARTI':6.987755839696382,'HDP':0.0,
                                              'DSP':0.5927800117471649},


                                  'BEYKOZ':{'SAADET':3.5255925821269214,'BTP':0.14588658960525192,
                                            'TKP':0.8051326074187863,'VATAN PARTISI':0.13208650680475512,
                                            'BBP':0.5250602932189021, 'CHP':36.71610601092178,
                                            'AK PARTI':49.15786637576968,'DP':0.20634409520742836,'MHP':0.0,
                                            'IYI PARTI':8.061219795890203,'HDP':0.6453181576232314,
                                            'DSP':0.20700124200745204},

                                  'BEYLIKDUZU':{'SAADET':0.7847357094115794,'BTP':0.1480237257886725,
                                                'TKP':0.12748647920458953,'VATAN PARTISI':0.19631515406015435,
                                                'BBP':0.5731982573093276,  'CHP':56.3272269172222,
                                                'AK PARTI':41.528528686158204,'DP':0.09710776337200147,
                                                'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':0.18424229699228387},


                                  'BEYOGLU':{'SAADET':2.9469157247912827,'BTP':0.20125651405352046,
                                             'TKP':0.1606214896855808,'VATAN PARTISI':0.17906473113507143,
                                             'BBP':1.5847993939347562, 'CHP':43.99100084940962,
                                             'AK PARTI':49.85957958049878,'DP':0.20890885299091666,
                                             'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':0.9519509638120892},


                                  'BUYUKCEKMECE':{'SAADET':0.6382435537401072,'BTP':0.15800840411511843,
                                                  'TKP':0.0,'VATAN PARTISI':0.11177887103340255,
                                                  'BBP':0.6755031774179081,'CHP':50.319121776870055,
                                                  'AK PARTI':47.46738057945615,'DP':0.0,'MHP':0.0,
                                                  'IYI PARTI':0.0,'HDP':0.0,'DSP':0.3946760137722609},


                                  'CATALCA':{'SAADET':0.7967636610058115,'BTP':0.14990656508614494,
                                             'TKP':0.23528762359500166,'VATAN PARTISI':0.22999363410477033,'BBP':0.0,
                                             'CHP':46.434071914080945,'AK PARTI':51.7465141589831,
                                             'DP':0.3778466846006941,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,
                                             'DSP':0.2649033821385301},


                                  'CEKMEKOY':{'SAADET':0.9097628537678827,'BTP':0.1243411645240842,'TKP':0.0,
                                              'VATAN PARTISI':0.20032743173324674,'BBP':0.0,'CHP':32.23337455012676,
                                              'AK PARTI':42.92118842521916,'DP':22.136871990771123,'MHP':0.0,
                                              'IYI PARTI':0.0,'HDP':0.711507774776704,'DSP':0.6410477815463896},



                                  'ESENLER':{'SAADET':4.451248520926601,'BTP':0.6570948762051144,
                                             'TKP':0.1215780275346601,'VATAN PARTISI':0.30374373299828,'BBP':0.0,
                                             'CHP':0.0, 'AK PARTI':65.47852853036015,'DP':0.326920965636703,
                                             'MHP':0.0,'IYI PARTI':17.321118525114766,'HDP':8.839877851917814,
                                             'DSP':0.9470135932436334},



                                  'ESENYURT':{'SAADET':0.9969396376947838,'BTP':0.19820999386115334,
                                              'TKP':0.32000845765682245,'VATAN PARTISI':0.10624055670957817,
                                              'BBP':0.6469574199628044,
                                              'CHP':51.516023295903736,'AK PARTI':45.95776201662245,
                                              'DP':0.23739894121884422,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,
                                              'DSP':0.30377097344892184},



                                  'EYUPSULTAN':{'SAADET':2.3372126574973553,'BTP':0.2679968872139691,
                                                'TKP':0.0,'VATAN PARTISI':0.19892101742635548,'BBP':0.0,
                                                'CHP':47.39697640053512,
                                                'AK PARTI':49.113380608042526,'DP':0.0,'MHP':0.0,'IYI PARTI':0.0,
                                                'HDP':0.0,'DSP':0.5058277300270183},


                                  'FATIH':{'SAADET':3.0824993137077,'BTP':0.2368290038758067,
                                           'TKP':0.0,'VATAN PARTISI':0.22100938475640114,'BBP':0.0,
                                           'CHP':36.081759513872406,
                                           'AK PARTI':53.03434253197656,'DP':0.2014675023147825,'MHP':0.0,
                                           'IYI PARTI':4.399249963940574,'HDP':2.1728712143418805,
                                           'DSP':0.3005727632687055},


                                  'GAZIOSMANPASA':{'SAADET':8.883435136707387,'BTP':0.23451134380453753,
                                                   'TKP':0.20984259478976192,'VATAN PARTISI':0.1537958115183246,
                                                   'BBP':1.4067044793484584,
                                                   'CHP':33.35405759162304,'AK PARTI':52.20913321698662,
                                                   'DP':0.19524432809773123,'MHP':0.0,'IYI PARTI':0.0,
                                                   'HDP':2.9010325770796976,
                                                   'DSP':0.4370273414776033},



                                 'GUNGOREN':{'SAADET':2.572244775221771,'BTP':0.323560366862126,
                                             'TKP':0.0,'VATAN PARTISI':0.11968125093970831,'BBP':1.2437227484588784,
                                             'CHP':37.06329875206736,'AK PARTI':53.78198767102691,
                                             'DP':0.18403247631935046,'MHP':0.0,'IYI PARTI':0.0,'HDP':4.081190798376184,
                                             'DSP':0.2995038340099233},



                                 'KADIKOY':{'SAADET':0.5934805426668367,'BTP':0.09057526739323073,
                                            'TKP':0.3307773267177868,'VATAN PARTISI':0.3466057163784281,
                                            'BBP':0.21940795819804268,
                                            'CHP':65.96985838213607,'AK PARTI':19.566219676087147,
                                            'DP':0.10561664753795497,'MHP':0.0,'IYI PARTI':12.666804001007117,
                                            'HDP':0.0,'DSP':0.0},


                                 'KAGITHANE':{'SAADET':3.504399531998782,'BTP':0.2428157004792204,'TKP':0.0,
                                              'VATAN PARTISI':0.20194573109162886,'BBP':2.112015770999952,
                                              'CHP':0.0,'AK PARTI':54.40353885852579,'DP':0.296908307021621,
                                              'MHP':0.0,'IYI PARTI':31.121279630727805,'HDP':5.452534739473979,
                                              'DSP':2.0775567772025707},


                                 'KARTAL':{'SAADET':1.4870210693099515,'BTP':0.17300618176396965,
                                           'TKP':0.4920423765486513,'VATAN PARTISI':0.2059432303963887,'BBP':0.0,
                                           'CHP':51.169265226450875,'AK PARTI':46.22454746228708,
                                           'DP':0.15081701215897153,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,
                                           'DSP':0.2610694486338059},



                                 'KUCUKCEKMECE':{'SAADET':1.5469392117933078,'BTP':0.2244676568715076,
                                                 'TKP':0.25621556778271254,'VATAN PARTISI':0.141457834421558,
                                                 'BBP':0.925843800530808,'CHP':50.98008446533715,
                                                 'AK PARTI':45.33837305296481,'DP':0.18011994350783592,
                                                 'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':0.5733363353323918},


                                 'MALTEPE':{'SAADET':1.5636931155974119,'BTP':0.2200356343858427,
                                            'TKP':0.0,'VATAN PARTISI':0.38916500328211445,'BBP':0.0,
                                            'CHP':52.72750411938859,
                                            'AK PARTI':0.0,'DP':0.3717497019304192,'MHP':42.879821024287644,
                                            'IYI PARTI':0.0,'HDP':0.0,'DSP':0.9729125082052863},


                                 'PENDIK':{'SAADET':2.8331784736696717,'BTP':0.2812586323799,'TKP':0.569681299985264,
                                           'VATAN PARTISI':0.24158107531202128,'BBP':0.0,
                                           'CHP':41.26641721704628,'AK PARTI':54.75553100123051,'DP':0.0,'MHP':0.0,
                                           'IYI PARTI':0.0,'HDP':0.0,'DSP':0.4449913362296276},

                                 'SANCAKTEPE':{'SAADET':1.7298675087646038,'BTP':0.19225583074527408,
                                               'TKP':0.0,'VATAN PARTISI':0.15571852354481475,'BBP':0.0,
                                               'CHP':47.17401327522162,
                                               'AK PARTI':49.89908743725587,'DP':0.21443919583126725,
                                               'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':0.2531513427460396},


                                 'SARIYER':{'SAADET':0.9568841551098004,'BTP':0.1199151819444783,
                                            'TKP':0.2170490034884429,'VATAN PARTISI':0.1603743693485096,'BBP':0.5888517877598771,
                                            'CHP':55.9652928416486,'AK PARTI':41.45116868556387,
                                            'DP':0.0,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':0.6000633698115967},


                                 'SILIVRI':{'SAADET':1.0640001601505416,'BTP':0.19818629511741034,
                                            'TKP':0.0,'VATAN PARTISI':0.32930955097791925,'BBP':0.3403199007066643,
                                            'CHP':43.97433587572318,'AK PARTI':0.0,'DP':0.561527836165996,
                                            'MHP':46.78397693832203,'IYI PARTI':0.0,'HDP':0.0,'DSP':6.695293575961404},


                                 'SULTANBEYLI':{'SAADET':6.072383793768537,'BTP':0.24124046546590291,
                                                'TKP':0.0,'VATAN PARTISI':0.0990600945149843,'BBP':7.357251490271715,
                                                'CHP':15.879915857190305,'AK PARTI':59.13945913188395,
                                                'DP':0.0,'MHP':0.0,'IYI PARTI':0.0,'HDP':10.601760938856614,
                                                'DSP':0.1952066568383514},

                                 'SULTANGAZI':{'SAADET':2.8384942849459924,'BTP':0.20255003509703196,
                                               'TKP':0.15033826108744675,
                                               'VATAN PARTISI':0.10721182892204967,'BBP':1.345910060799933,
                                               'CHP':29.877177849407545,'AK PARTI':58.573977908077204,
                                               'DP':0.21372520944721302,
                                               'MHP':0.0,'IYI PARTI':0.0,'HDP':6.467632155167295,
                                               'DSP':0.2902053089062647},



                                 'SILE':{'SAADET':0.5245797400945833,'BTP':0.09935222350276199,
                                         'TKP':0.0,'VATAN PARTISI':0.21857489170607636,'BBP':0.0,
                                         'CHP':11.143345388069784,'AK PARTI':54.36553670071136,
                                         'DP':0.0,'MHP':0.0,'IYI PARTI':33.445932519969794,'HDP':0.0,
                                         'DSP':0.16293764654452966},

                                 'SISLI':{'SAADET':0.6818224624715122,'BTP':0.0860125942528519,
                                          'TKP':0.0,'VATAN PARTISI':0.16700255526466137,'BBP':0.4200177047821747,
                                          'CHP':48.49477960057509,'AK PARTI':20.877830724703195,'DP':0.0,
                                          'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,'DSP':28.892069889941553},


                                 'TUZLA':{'SAADET':1.608984175599796,'BTP':0.15994555045091033,
                                          'TKP':0.3804644680089654,'VATAN PARTISI':0.1633486472690148,
                                          'BBP':1.0352220520673814,'CHP':46.22222222222222,
                                          'AK PARTI':50.52033350348818,'DP':0.0,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,
                                          'DSP':0.28994384890250124},


                                 'UMRANIYE':{'SAADET':3.0701366330877056,'BTP':0.22422488213658254,
                                             'TKP':0.0,'VATAN PARTISI':0.1675998837165211,'BBP':1.471997168750079,
                                             'CHP':37.51178634174703,'AK PARTI':54.566528053389284,
                                             'DP':0.26644084078011043,'MHP':0.0,'IYI PARTI':0.0,
                                             'HDP':2.3208665647079645,'DSP':0.4004196316847201},


                                 'USKUDAR':{'SAADET':4.564190938854379,'BTP':0.2513787975613228,
                                            'TKP':0.0,'VATAN PARTISI':0.23744696058804465,'BBP':0.0,
                                            'CHP':45.50501394698027,
                                            'AK PARTI':48.3465029574867,'DP':0.0,'MHP':0.0,'IYI PARTI':0.0,
                                            'HDP':0.0,'DSP':0.9437305219290143},


                                 'ZEYTINBURNU':{'SAADET':2.2366042951307676,'BTP':0.32426110992983204,
                                                'TKP':0.0,'VATAN PARTISI':0.18605145651711674,'BBP':0.0,
                                                'CHP':46.0783010844142,'AK PARTI':50.42326706357644,
                                                'DP':0.20332766319370613,'MHP':0.0,'IYI PARTI':0.0,'HDP':0.0,
                                                'DSP':0.5481873272379333}}



        self.political_party_total_percentages = {'SAADET': 2.472071279821189, 'BTP': 0.23420285958540843,
                                             'TKP': 0.14923868317079167, 'VATAN PARTISI': 0.19185496833301943,
                                             'BBP': 0.8182746845963134, 'CHP': 40.20182521861851,
                                             'AK PARTI': 45.797779892255015, 'DP': 0.5830565958736887,
                                             'MHP': 2.2502262093887926,
                                             'IYI PARTI': 3.701128678075975, 'HDP': 2.1128902126543294,
                                             'DSP': 1.2931568655045445}
        self.election_resultsDistric = {
            'SAADET': {'ADALAR': 0.4309912799438709, 'ARNAVUTKOY': 2.8034945886034683, 'ATASEHIR': 1.621149571292474,
                       'AVCILAR': 0.7434423358265851,
                       'BAGCILAR': 3.8421486582232522, 'BAHCELIEVLER': 1.7867766161095568,
                       'BAKIRKOY': 0.8340947272244982, 'BASAKSEHIR': 3.282132620975596,
                       'BAYRAMPASA': 836294803688099, 'BESIKTAS': 0.7590475760177111, 'BEYKOZ': 3.5255925821269214,
                       'BEYLIKDUZU': 0.7847357094115794,
                       'BEYOGLU': 2.9469157247912827, 'BUYUKCEKMECE': 0.6382435537401072, 'CATALCA': 0.7967636610058115,
                       'CEKMEKOY': 0.9097628537678827,
                       'ESENLER': 4.451248520926601, 'ESENYURT': 0.9969396376947838, 'EYUPSULTAN': 2.3372126574973553,
                       'FATIH': 3.0824993137077,
                       'GAZIOSMANPASA': 8.883435136707387, 'GUNGOREN': 2.572244775221771, 'KADIKOY': 0.5934805426668367,
                       'KAGITHANE': 3.504399531998782,
                       'KARTAL': 1.4870210693099515, 'KUCUKCEKMECE': 1.5469392117933078, 'MALTEPE': 1.5636931155974119,
                       'PENDIK': 2.8331784736696717,
                       'SANCAKTEPE': 1.7298675087646038, 'SARIYER': 0.9568841551098004, 'SILIVRI': 1.0640001601505416,
                       'SULTANBEYLI': 6.072383793768537,
                       'SULTANGAZI': 2.8384942849459924, 'SILE': 0.5245797400945833, 'SISLI': 0.6818224624715122,
                       'TUZLA': 1.608984175599796,
                       'UMRANIYE': 3.0701366330877056, 'USKUDAR': 4.564190938854379, 'ZEYTINBURNU': 2.2366042951307676},

            'BTP': {'ADALAR': 0.07016137115365341, 'ARNAVUTKOY': 0.8758204024861999, 'ATASEHIR': 0.16910130200063514,
                    'AVCILAR': 0.11909913251323895,
                    'BAGCILAR': 0.32249036184981883, 'BAHCELIEVLER': 0.2647621852451774,
                    'BAKIRKOY': 0.14810339237820153, 'BASAKSEHIR': 0.24023522646112178,
                    'BAYRAMPASA': 0.27355437503816327, 'BESIKTAS': 0.10933899606921792, 'BEYKOZ': 0.14588658960525192,
                    'BEYLIKDUZU': 0.1480237257886725,
                    'BEYOGLU': 0.20125651405352046, 'BUYUKCEKMECE': 0.15800840411511843, 'CATALCA': 0.14990656508614494,
                    'CEKMEKOY': 0.1243411645240842,
                    'ESENLER': 0.6570948762051144, 'ESENYURT': 0.19820999386115334, 'EYUPSULTAN': 0.2679968872139691,
                    'FATIH': 0.2368290038758067,
                    'GAZIOSMANPASA': 0.23451134380453753, 'GUNGOREN': 0.323560366862126, 'KADIKOY': 0.09057526739323073,
                    'KAGITHANE': 0.2428157004792204,
                    'KARTAL': 0.17300618176396965, 'KUCUKCEKMECE': 0.2244676568715076, 'MALTEPE': 0.2200356343858427,
                    'PENDIK': 0.2812586323799,
                    'SANCAKTEPE': 0.19225583074527408, 'SARIYER': 0.1199151819444783, 'SILIVRI': 0.19818629511741034,
                    'SULTANBEYLI': 0.24124046546590291,
                    'SULTANGAZI': 0.20255003509703196, 'SILE': 0.09935222350276199, 'SISLI': 0.0860125942528519,
                    'TUZLA': 0.15994555045091033,
                    'UMRANIYE': 0.22422488213658254, 'USKUDAR': 0.2513787975613228, 'ZEYTINBURNU': 0.32426110992983204},

            'TKP': {'ADALAR': 0.0, 'ARNAVUTKOY': 0.21732516190724563, 'ATASEHIR': 0.6093204191806922,
                    'AVCILAR': 0.0, 'BAGCILAR': 0.5481873272379333, 'BAHCELIEVLER': 0.3635896026485057,
                    'BAKIRKOY': 0.0, 'BASAKSEHIR': 0.5784137463526777, 'BAYRAMPASA': 0.0,
                    'BESIKTAS': 0.0, 'BEYKOZ': 0.8051326074187863, 'BEYLIKDUZU': 0.12748647920458953,
                    'BEYOGLU': 0.1606214896855808, 'BUYUKCEKMECE': 0.0, 'CATALCA': 0.23528762359500166,
                    'CEKMEKOY': 0.0, 'ESENLER': 0.1215780275346601, 'ESENYURT': 0.32000845765682245,
                    'EYUPSULTAN': 0.0, 'FATIH': 0.0, 'GAZIOSMANPASA': 0.20984259478976192,
                    'GUNGOREN': 0.0, 'KADIKOY': 0.3307773267177868, 'KAGITHANE': 0.0,
                    'KARTAL': 0.4920423765486513, 'KUCUKCEKMECE': 0.25621556778271254, 'MALTEPE': 0.0,
                    'PENDIK': 0.569681299985264, 'SANCAKTEPE': 0.0, 'SARIYER': 0.2170490034884429,
                    'SILIVRI': 0.0, 'SULTANBEYLI': 0.0, 'SULTANGAZI': 0.15033826108744675,
                    'SILE': 0.0, 'SISLI': 0.0, 'TUZLA': 0.3804644680089654,
                    'UMRANIYE': 0.0, 'USKUDAR': 0.0, 'ZEYTINBURNU': 0.0},

            'VATAN PARTISI': {'ADALAR': 0.2906685376365641, 'ARNAVUTKOY': 0.15212761333507194,
                              'ATASEHIR': 0.28739282311845027, 'AVCILAR': 0.12692917928746575,
                              'BAGCILAR': 0.21179976853311008, 'BAHCELIEVLER': 0.1493152702105728, 'BAKIRKOY': 0.0,
                              'BASAKSEHIR': 0.1535093821595199,
                              'BAYRAMPASA': 0.15509556084753007, 'BESIKTAS': 0.37229476347535356,
                              'BEYKOZ': 0.13208650680475512, 'BEYLIKDUZU': 0.19631515406015435,
                              'BEYOGLU': 0.17906473113507143, 'BUYUKCEKMECE': 0.11177887103340255,
                              'CATALCA': 0.22999363410477033, 'CEKMEKOY': 0.20032743173324674,
                              'ESENLER': 0.30374373299828, 'ESENYURT': 0.10624055670957817,
                              'EYUPSULTAN': 0.19892101742635548, 'FATIH': 0.22100938475640114,
                              'GAZIOSMANPASA': 0.1537958115183246, 'GUNGOREN': 0.11968125093970831,
                              'KADIKOY': 0.3466057163784281, 'KAGITHANE': 0.20194573109162886,
                              'KARTAL': 0.2059432303963887, 'KUCUKCEKMECE': 0.141457834421558,
                              'MALTEPE': 0.38916500328211445, 'PENDIK': 0.24158107531202128,
                              'SANCAKTEPE': 0.15571852354481475, 'SARIYER': 0.1603743693485096,
                              'SILIVRI': 0.32930955097791925, 'SULTANBEYLI': 0.0990600945149843,
                              'SULTANGAZI': 0.10721182892204967, 'SILE': 0.21857489170607636,
                              'SISLI': 0.16700255526466137, 'TUZLA': 0.1633486472690148,
                              'UMRANIYE': 0.1675998837165211, 'USKUDAR': 0.23744696058804465,
                              'ZEYTINBURNU': 0.18605145651711674},

            'BBP': {'ADALAR': 0.0, 'ARNAVUTKOY': 1.164138450616479, 'ATASEHIR': 0.0, 'AVCILAR': 0.3770785683377635,
                    'BAGCILAR': 2.364340987541635, 'BAHCELIEVLER': 1.1488735090561035, 'BAKIRKOY': 0.0,
                    'BASAKSEHIR': 1.0541595941044977,
                    'BAYRAMPASA': 1.189473041460585, 'BESIKTAS': 0.28283558487326615, 'BEYKOZ': 0.5250602932189021,
                    'BEYLIKDUZU': 0.5731982573093276,
                    'BEYOGLU': 1.5847993939347562, 'BUYUKCEKMECE': 0.6755031774179081, 'CATALCA': 0.0, 'CEKMEKOY': 0.0,
                    'ESENLER': 0.0, 'ESENYURT': 0.6469574199628044, 'EYUPSULTAN': 0.0, 'FATIH': 0.0,
                    'GAZIOSMANPASA': 1.4067044793484584, 'GUNGOREN': 1.2437227484588784, 'KADIKOY': 0.21940795819804268,
                    'KAGITHANE': 2.112015770999952,
                    'KARTAL': 0.0, 'KUCUKCEKMECE': 0.925843800530808, 'MALTEPE': 0.0, 'PENDIK': 0.0,
                    'SANCAKTEPE': 0.0, 'SARIYER': 0.5888517877598771, 'SILIVRI': 0.3403199007066643,
                    'SULTANBEYLI': 7.357251490271715,
                    'SULTANGAZI': 1.345910060799933, 'SILE': 0.0, 'SISLI': 0.4200177047821747,
                    'TUZLA': 1.0352220520673814, 'UMRANIYE': 1.471997168750079,
                    'USKUDAR': 0.0, 'ZEYTINBURNU': 0.0},

            'CHP': {'ADALAR': 44.10143329658214, 'ARNAVUTKOY': 0.0, 'ATASEHIR': 51.35876468720228,
                    'AVCILAR': 52.126269806927525,
                    'BAGCILAR': 0.0, 'BAHCELIEVLER': 45.22986305404211, 'BAKIRKOY': 56.9741224321377,
                    'BASAKSEHIR': 36.752279452003975,
                    'BAYRAMPASA': 44.573487207669295, 'BESIKTAS': 73.06284733203813, 'BEYKOZ': 36.71610601092178,
                    'BEYLIKDUZU': 56.3272269172222,
                    'BEYOGLU': 43.99100084940962, 'BUYUKCEKMECE': 50.319121776870055, 'CATALCA': 46.434071914080945,
                    'CEKMEKOY': 32.23337455012676,
                    'ESENLER': 0.0, 'ESENYURT': 51.516023295903736, 'EYUPSULTAN': 47.39697640053512,
                    'FATIH': 36.081759513872406,
                    'GAZIOSMANPASA': 33.35405759162304, 'GUNGOREN': 37.06329875206736, 'KADIKOY': 65.96985838213607,
                    'KAGITHANE': 0.0,
                    'KARTAL': 51.169265226450875, 'KUCUKCEKMECE': 50.98008446533715, 'MALTEPE': 52.72750411938859,
                    'PENDIK': 41.26641721704628,
                    'SANCAKTEPE': 47.17401327522162, 'SARIYER': 55.9652928416486, 'SILIVRI': 43.97433587572318,
                    'SULTANBEYLI': 15.879915857190305,
                    'SULTANGAZI': 29.877177849407545, 'SILE': 11.143345388069784, 'SISLI': 48.49477960057509,
                    'TUZLA': 46.22222222222222,
                    'UMRANIYE': 37.51178634174703, 'USKUDAR': 45.50501394698027, 'ZEYTINBURNU': 46.0783010844142},

            'AK PARTI': {'ADALAR': 30.74070361832214, 'ARNAVUTKOY': 57.7324292606598, 'ATASEHIR': 45.14250555731979,
                         'AVCILAR': 45.47402691063444, 'BAGCILAR': 57.890171734312325,
                         'BAHCELIEVLER': 49.893977322927405,
                         'BAKIRKOY': 24.846738778036485, 'BASAKSEHIR': 54.75229800298671,
                         'BAYRAMPASA': 49.288025889967635,
                         'BESIKTAS': 0.0, 'BEYKOZ': 49.15786637576968, 'BEYLIKDUZU': 41.528528686158204,
                         'BEYOGLU': 49.85957958049878, 'BUYUKCEKMECE': 47.46738057945615, 'CATALCA': 51.7465141589831,
                         'CEKMEKOY': 42.92118842521916, 'ESENLER': 65.47852853036015, 'ESENYURT': 45.95776201662245,
                         'EYUPSULTAN': 49.113380608042526, 'FATIH': 53.03434253197656,
                         'GAZIOSMANPASA': 52.20913321698662,
                         'GUNGOREN': 53.78198767102691, 'KADIKOY': 19.566219676087147, 'KAGITHANE': 54.40353885852579,
                         'KARTAL': 46.22454746228708,
                         'KUCUKCEKMECE': 45.33837305296481, 'MALTEPE': 0.0, 'PENDIK': 54.75553100123051,
                         'SANCAKTEPE': 49.89908743725587,
                         'SARIYER': 41.45116868556387, 'SILIVRI': 0.0, 'SULTANBEYLI': 59.13945913188395,
                         'SULTANGAZI': 58.573977908077204,
                         'SILE': 54.36553670071136, 'SISLI': 20.877830724703195, 'TUZLA': 50.52033350348818,
                         'UMRANIYE': 54.566528053389284,
                         'USKUDAR': 48.3465029574867, 'ZEYTINBURNU': 50.42326706357644},

            'DP': {'ADALAR': 0.0, 'ARNAVUTKOY': 0.3325074977180858, 'ATASEHIR': 0.15123848840901874,
                   'AVCILAR': 0.17267313675794854,
                   'BAGCILAR': 0.3393839148161502, 'BAHCELIEVLER': 1.1883375055220144, 'BAKIRKOY': 0.3802057237171741,
                   'BASAKSEHIR': 0.0,
                   'BAYRAMPASA': 0.0, 'BESIKTAS': 0.2277142728053133, 'BEYKOZ': 0.20634409520742836,
                   'BEYLIKDUZU': 0.09710776337200147,
                   'BEYOGLU': 0.20890885299091666, 'BUYUKCEKMECE': 0.0, 'CATALCA': 0.3778466846006941,
                   'CEKMEKOY': 22.136871990771123,
                   'ESENLER': 0.326920965636703, 'ESENYURT': 0.23739894121884422, 'EYUPSULTAN': 0.0,
                   'FATIH': 0.2014675023147825,
                   'GAZIOSMANPASA': 0.19524432809773123, 'GUNGOREN': 0.18403247631935046,
                   'KADIKOY': 0.10561664753795497, 'KAGITHANE': 0.296908307021621,
                   'KARTAL': 0.15081701215897153, 'KUCUKCEKMECE': 0.18011994350783592, 'MALTEPE': 0.3717497019304192,
                   'PENDIK': 0.0,
                   'SANCAKTEPE': 0.21443919583126725, 'SARIYER': 0.0, 'SILIVRI': 0.561527836165996, 'SULTANBEYLI': 0.0,
                   'SULTANGAZI': 0.21372520944721302, 'SILE': 0.0, 'SISLI': 0.0, 'TUZLA': 0.0,
                   'UMRANIYE': 0.26644084078011043, 'USKUDAR': 0.0, 'ZEYTINBURNU': 0.20332766319370613},

            'MHP': {'ADALAR': 0.0, 'ARNAVUTKOY': 0.0, 'ATASEHIR': 0.0, 'AVCILAR': 0.0,
                    'BAGCILAR': 0.0, 'BAHCELIEVLER': 0.0, 'BAKIRKOY': 0.0, 'BASAKSEHIR': 0.0,
                    'BAYRAMPASA': 0.0, 'BESIKTAS': 16.3186192563141, 'BEYKOZ': 0.0, 'BEYLIKDUZU': 0.0,
                    'BEYOGLU': 0.0, 'BUYUKCEKMECE': 0.0, 'CATALCA': 0.0, 'CEKMEKOY': 0.0,
                    'ESENLER': 0.0, 'ESENYURT': 0.0, 'EYUPSULTAN': 0.0, 'FATIH': 0.0,
                    'GAZIOSMANPASA': 0.0, 'GUNGOREN': 0.0, 'KADIKOY': 0.0, 'KAGITHANE': 0.0,
                    'KARTAL': 0.0, 'KUCUKCEKMECE': 0.0, 'MALTEPE': 42.879821024287644, 'PENDIK': 0.0,
                    'SANCAKTEPE': 0.0, 'SARIYER': 0.0, 'SILIVRI': 46.78397693832203, 'SULTANBEYLI': 0.0,
                    'SULTANGAZI': 0.0, 'SILE': 0.0, 'SISLI': 0.0, 'TUZLA': 0.0,
                    'UMRANIYE': 0.0, 'USKUDAR': 0.0, 'ZEYTINBURNU': 0.0},

            'IYI PARTI': {'ADALAR': 0.0, 'ARNAVUTKOY': 19.150693267266483, 'ATASEHIR': 0.0, 'AVCILAR': 0.0,
                          'BAGCILAR': 20.492384033323162, 'BAHCELIEVLER': 0.0, 'BAKIRKOY': 9.270830263196675,
                          'BASAKSEHIR': 0.0,
                          'BAYRAMPASA': 0.0, 'BESIKTAS': 6.98775583966382, 'BEYKOZ': 8.061219795890203,
                          'BEYLIKDUZU': 0.0,
                          'BEYOGLU': 0.0, 'BUYUKCEKMECE': 0.0, 'CATALCA': 0.0, 'CEKMEKOY': 0.0,
                          'ESENLER': 17.321118525114766, 'ESENYURT': 0.0, 'EYUPSULTAN': 0.0, 'FATIH': 4.399249963940574,
                          'GAZIOSMANPASA': 0.0, 'GUNGOREN': 0.0, 'KADIKOY': 12.666804001007117,
                          'KAGITHANE': 31.121279630727805,
                          'KARTAL': 0.0, 'KUCUKCEKMECE': 0.0, 'MALTEPE': 0.0, 'PENDIK': 0.0,
                          'SANCAKTEPE': 0.0, 'SARIYER': 0.0, 'SILIVRI': 0.0, 'SULTANBEYLI': 0.0,
                          'SULTANGAZI': 0.0, 'SILE': 33.445932519969794, 'SISLI': 0.0, 'TUZLA': 0.0,
                          'UMRANIYE': 0.0, 'USKUDAR': 0.0, 'ZEYTINBURNU': 0.0},

            'HDP': {'ADALAR': 0.0, 'ARNAVUTKOY': 13.729879312093422, 'ATASEHIR': 0.0, 'AVCILAR': 0.0,
                    'BAGCILAR': 12.806826003968725, 'BAHCELIEVLER': 0.0, 'BAKIRKOY': 0.0,
                    'BASAKSEHIR': 3.3976124885215793,
                    'BAYRAMPASA': 0.7956280148989436, 'BESIKTAS': 0.0, 'BEYKOZ': 0.6453181576232314, 'BEYLIKDUZU': 0.0,
                    'BEYOGLU': 0.0, 'BUYUKCEKMECE': 0.0, 'CATALCA': 0.0, 'CEKMEKOY': 0.711507774776704,
                    'ESENLER': 8.839877851917814, 'ESENYURT': 0.0, 'EYUPSULTAN': 0.0, 'FATIH': 2.1728712143418805,
                    'GAZIOSMANPASA': 2.9010325770796976, 'GUNGOREN': 4.081190798376184, 'KADIKOY': 0.0,
                    'KAGITHANE': 5.452534739473979,
                    'KARTAL': 0.0, 'KUCUKCEKMECE': 0.0, 'MALTEPE': 0.0, 'PENDIK': 0.0,
                    'SANCAKTEPE': 0.0, 'SARIYER': 0.0, 'SILIVRI': 0.0, 'SULTANBEYLI': 10.601760938856614,
                    'SULTANGAZI': 6.467632155167295, 'SILE': 0.0, 'SISLI': 0.0, 'TUZLA': 0.0,
                    'UMRANIYE': 2.3208665647079645, 'USKUDAR': 0.0, 'ZEYTINBURNU': 0.0},

            'DSP': {'ADALAR': 24.366041896361633, 'ARNAVUTKOY': 0.6657394126425291, 'ATASEHIR': 0.5251667195935218,
                    'AVCILAR': 0.7982526632461726,
                    'BAGCILAR': 1.2539050582323292, 'BAHCELIEVLER': 0.33809453688705643, 'BAKIRKOY': 6.632968846709304,
                    'BASAKSEHIR': 0.28290248675923607,
                    'BAYRAMPASA': 0.5745863100689992, 'BESIKTAS': 0.5927800117471649, 'BEYKOZ': 0.20700124200745204,
                    'BEYLIKDUZU': 0.18424229699228387,
                    'BEYOGLU': 0.9519509638120892, 'BUYUKCEKMECE': 0.3946760137722609, 'CATALCA': 0.2649033821385301,
                    'CEKMEKOY': 0.6410477815463896,
                    'ESENLER': 0.9470135932436334, 'ESENYURT': 0.30377097344892184, 'EYUPSULTAN': 0.5058277300270183,
                    'FATIH': 0.3005727632687055,
                    'GAZIOSMANPASA': 0.4370273414776033, 'GUNGOREN': 0.2995038340099233, 'KADIKOY': 0.4414318085951678,
                    'KAGITHANE': 2.0775567772025707,
                    'KARTAL': 0.2610694486338059, 'KUCUKCEKMECE': 0.5733363353323918, 'MALTEPE': 0.9729125082052863,
                    'PENDIK': 0.4449913362296276,
                    'SANCAKTEPE': 0.2531513427460396, 'SARIYER': 0.6000633698115967, 'SILIVRI': 6.695293575961404,
                    'SULTANBEYLI': 0.1952066568383514,
                    'SULTANGAZI': 0.2902053089062647, 'SILE': 0.16293764654452966, 'SISLI': 28.892069889941553,
                    'TUZLA': 0.28994384890250124,
                    'UMRANIYE': 0.4004196316847201, 'USKUDAR': 0.9437305219290143, 'ZEYTINBURNU': 0.5481873272379333}}
        self.districts = {}
        self.political_parties = {}
        self.district_names = []
        self.political_party_names=[]
        self.total_vote_count = 0
        self.political_party_vote_percentages = {}
        self.district_vote_percentages={}
        self.party_names_dict={}
        self.district_names_dict={}
        self.saadet_vote_percentage=[]
        self.btp_vote_percentage = []
        self.tkp_vote_percentage = []
        self.vatan_vote_percentage = []
        self.bbp_vote_percentage = []
        self.chp_vote_percentage = []
        self.ak_vote_percentage = []
        self.dp_vote_percentage = []
        self.mhp_vote_percentage = []
        self.iyi_vote_percentage = []
        self.hdp_vote_percentage = []
        self.dsp_vote_percentage = []


    def parse_data(self,file_path):
        workbook = xlrd.open_workbook(file_path)
        worksheet = workbook.sheet_by_index(0)

        #reading the party names as list and dictionary
        for i in range(9, 21):
            party = worksheet.cell_value(10, i)
            self.political_party_names.append(party)
            self.party_names_dict.setdefault(party,'')

        #reading the district names as list and dictionary
        for i in range(11, 50):
            district = worksheet.cell_value(i, 2)
            self.district_names.append(district)
            self.district_names_dict.setdefault(district,'')

        #combing district names dict with party names dict
        for name in self.district_names:
            self.political_party_vote_percentages[name]=self.party_names_dict
        #print(self.political_party_vote_percentages)

        #combing party names dict with district names dict
        for name in self.political_party_names:
            self.district_vote_percentages[name]=self.district_names_dict
        #print(self.district_vote_percentages)

        #reading and calulating vote percenytage for districts per parties
        for i in range(11,50):
            vote=worksheet.cell_value(i,9)
            total_vote_count=worksheet.cell_value(i,7)
            self.saadet_vote_percentage.append(((vote/float(total_vote_count))*100))


        for i in range(11,50):
            vote=worksheet.cell_value(i,10)
            total_vote_count=worksheet.cell_value(i,7)
            self.btp_vote_percentage.append(((vote/float(total_vote_count))*100))



        for i in range(11,50):
            vote=worksheet.cell_value(i,11)
            total_vote_count=worksheet.cell_value(i,7)
            self.tkp_vote_percentage.append(((vote/float(total_vote_count))*100))



        for i in range(11,50):
            vote=worksheet.cell_value(i,12)
            total_vote_count=worksheet.cell_value(i,7)
            self.vatan_vote_percentage.append(((vote/float(total_vote_count))*100))



        for i in range(11,50):
            vote=worksheet.cell_value(i,13)
            total_vote_count=worksheet.cell_value(i,7)
            self.bbp_vote_percentage.append(((vote/float(total_vote_count))*100))



        for i in range(11,50):
            vote=worksheet.cell_value(i,14)
            total_vote_count=worksheet.cell_value(i,7)
            self.chp_vote_percentage.append(((vote/float(total_vote_count))*100))


        for i in range(11,50):
            vote=worksheet.cell_value(i,15)
            total_vote_count=worksheet.cell_value(i,7)
            self.ak_vote_percentage.append(((vote/float(total_vote_count))*100))


        for i in range(11,50):
            vote=worksheet.cell_value(i,16)
            total_vote_count=worksheet.cell_value(i,7)
            self.dp_vote_percentage.append(((vote/float(total_vote_count))*100))


        for i in range(11,50):
            vote=worksheet.cell_value(i,17)
            total_vote_count=worksheet.cell_value(i,7)
            self.mhp_vote_percentage.append(((vote/float(total_vote_count))*100))


        for i in range(11,50):
            vote=worksheet.cell_value(i,18)
            total_vote_count=worksheet.cell_value(i,7)
            self.iyi_vote_percentage.append(((vote/float(total_vote_count))*100))


        for i in range(11,50):
            vote=worksheet.cell_value(i,19)
            total_vote_count=worksheet.cell_value(i,7)
            self.hdp_vote_percentage.append(((vote/float(total_vote_count))*100))

        for i in range(11,50):
            vote=worksheet.cell_value(i,20)
            total_vote_count=worksheet.cell_value(i,7)
            self.dsp_vote_percentage.append(((vote/float(total_vote_count))*100))

    def cluster_districts(self,selected_districts,threshold=0):
        self.party_names1=[]
        assert self.district_names!=[] and self.political_party_names!=[]

        if not selected_districts:
            selected_districts=self.district_names

        for political_party in self.political_party_names:
            if self.political_party_total_percentages[political_party]>=threshold:
                self.party_names1.append(political_party)

        cluster_matrix = [[0.0] * len(self.party_names1) for i in range(len(selected_districts))]



        for i in range(len(selected_districts)):
            for j in range(len(self.party_names1)):
                cluster_matrix[i][j] = self.election_resultsDistric[self.party_names1[j]][selected_districts[i]]

        cluster = hcluster(cluster_matrix, distance=sim_distance)

        drawdendrogram(cluster, selected_districts)

    def cluster_political_parties(self,selected_districts,threshold=0):
        self.party_names2=[]
        assert self.district_names!=[] and self.political_party_names!=[]

        if not selected_districts:
            selected_districts=self.district_names

        for political_party in self.political_party_names:
            if self.political_party_total_percentages[political_party]>=threshold:
               self.party_names2.append(political_party)

        cluster_matrix = [[0.0] * len(selected_districts) for i in range(len(self.party_names2))]

        for i in range(len(self.party_names2)):
            for j in range(len(selected_districts)):
                cluster_matrix[i][j]=self.election_resultsDistric[self.party_names2[i]][selected_districts[j]]


        cluster=hcluster(cluster_matrix,distance=sim_distance)

        drawdendrogram(cluster,self.party_names2)







class District:

    def __init__(self,name):
        self.name=name
        self.election_results={}
    def add_political_party(self,acronym,vote_percentage):
        self.election_results[acronym]=vote_percentage
    def get_political_party_percentage(self,acronym):
        try:
            return self.election_results[acronym]
        except KeyError:
            return 0.0


class PoliticalParty:
    def __init__(self,acronym):
        self.acronym=acronym
        self.election_results={}
        self.vote_count=0
    def add_district(self,name,vote_percentage,count):
        self.election_results[name] = vote_percentage
        self.vote_count += count

    def get_district_percentage(self, district_name):
        try:
            self.election_results[district_name]
        except KeyError:
            return ' '





def main():
    data_center=DataCenter()
    g=PCluster(data_center)
    g.interface()
main()







































