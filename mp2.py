from tkinter import *
from recommendations import *
import csv



class Reco(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.engine = [('Movie Based',True),('User Based    ',False)]
        self.similarityM = [('Person     ',True),('Euclideon',False)]
        self.user_id=[]
        self.movie_ti=[]
        self.prefs={}
        self.initUI()

    def initUI(self):
        r1=2
        r2=5
        Grid.rowconfigure(self,0,pad=3)
        Grid.rowconfigure(self,1,pad=3)
        Grid.rowconfigure(self,2,pad=3)
        Grid.rowconfigure(self,3,pad=3)
        Grid.rowconfigure(self,4,pad=3)
        Grid.rowconfigure(self,5,pad=3)
        Grid.rowconfigure(self,6,pad=3)
        Grid.rowconfigure(self,7,pad=3)
        Grid.rowconfigure(self,8,pad=3)
        Grid.rowconfigure(self,9,pad=3)
        Grid.rowconfigure(self,10,pad=3)

        Grid.columnconfigure(self,0,pad=3)
        Grid.columnconfigure(self,1,pad=3)
        Grid.columnconfigure(self,2,pad=3)
        Grid.columnconfigure(self,3,pad=3)
        Grid.columnconfigure(self,4,pad=3)


        self.var1=BooleanVar()
        self.var2=BooleanVar()


        self.mainL=Label(self,text='Movie Recommendation Engine',font=('Times',11,'bold'))
        self.mainL.grid(in_=self,row=0,column=0,columnspan=5)

        self.upRatingsB = Button(self, text='Upload Ratings',command=self.uploadRatings)
        self.upRatingsB.grid(in_=self,row=7,column=0)

        self.upMoviesB = Button(self, text='Upload Movies',command=self.uploadMovies)
        self.upMoviesB.grid(in_=self, row=8, column=0)

        self.upLinksB = Button(self, text=' Upload Links   ',command=self.uploadLinks)
        self.upLinksB.grid(in_=self, row=9, column=0)



        self.engineL=Label(self,text='Engine',font=('Times',10,'bold'))
        self.engineL.grid(in_=self,row=1,column=0)

        for text, mode in self.engine:
            self.engineR=Radiobutton(self,text=text,variable=self.var1, value=mode,command=self.engine_result)
            self.engineR.grid(in_=self,row=r1,column=0)
            r1=r1+1


        self.simiL=Label(self,text='Similarity Metric',font=('Times',10,'bold'))
        self.simiL.grid(in_=self,row=4,column=0)

        for text, mode in self.similarityM:
            self.simiR=Radiobutton(self,text=text,variable=self.var2, value=mode,command=self.mania)
            self.simiR.grid(in_=self,row=r2,column=0)
            r2=r2+1


        self.listlb=Label(self,text='Movies/Users',font=('Times',10,'bold'))
        self.listlb.grid(in_=self,row=1,column=1)

        self.lb1=Listbox(self,selectmode='browse')
        for item in self.user_id:
            self.lb1.insert(END,item)
        self.lb1.grid(in_=self,row=2,column=1,rowspan=5)

        self.listlb2=Label(self,text='Recommended Movies',font=('Times',10,'bold'))
        self.listlb2.grid(in_=self,row=1,column=2)

        self.lb2=Listbox(self,selectmode='browse')
        for item in self.movie_ti:
            self.lb2.insert(END,item)
        self.lb2.grid(in_=self,row=2,column=2,rowspan=5)

        self.infoL = Label(self,text='Information',font=('Times',10,'bold'))
        self.infoL.grid(in_=self,row=1,column=3)

        self.directorL = Label(self,text='Director:')
        self.directorL.grid(in_=self,row=2,column=3)

        self.starsL = Label(self,text='Stars:')
        self.starsL.grid(in_=self,row=3,column=3)

        self.ratinL = Label(self,text='Ratings:')
        self.ratinL.grid(in_=self,row=4,column=3)

        self.genreL = Label(self,text='Genre:')
        self.genreL.grid(in_=self,row=5,column=3)

        self.plotL = Label(self,text='Plot:')
        self.plotL.grid(in_=self,row=6,column=3)

        self.taglinesL = Label(self,text=':taglines:')
        self.taglinesL.grid(in_=self,row=7,column=3)

        self.trailerL = Label(self,text='Trailer(Link):')
        self.trailerL.grid(in_=self,row=8,column=3)


        self.directorE = Entry(self)
        self.directorE.grid(in_=self, row=2, column=4)

        self.starsE = Entry(self)
        self.starsE.grid(in_=self, row=3, column=4)

        self.ratingE = Entry(self)
        self.ratingE.grid(in_=self, row=4, column=4)

        self.genreE = Entry(self)
        self.genreE.grid(in_=self, row=5, column=4)

        self.plotE = Entry(self)
        self.plotE.grid(in_=self, row=6, column=4)

        self.taglinesE = Entry(self)
        self.taglinesE.grid(in_=self, row=7, column=4)

        self.trailerE = Entry(self)
        self.trailerE.grid(in_=self, row=8, column=4)

        self.pack()

    def engine_result(self):
        engineresult=self.var1.get()
        if engineresult==True:
            for key in self.movies:
                for name in self.movies[key]:
                    self.user_id.append(name)
            self.lb1.configure(selectmode='browse')
            for item in self.user_id:
                self.lb1.insert(END, item)
            self.listlb.configure(text='Movies')

        else:
            for key in self.ratings:
                self.user_id.append(key)
            self.lb1.configure(selectmode='browse')
            for item in self.user_id:
                self.lb1.insert(END, item)
            self.listlb.configure(text='Users')





    def mania(self):
        simres=self.var2.get()
        user_or_movie=str(self.lb1.get(ANCHOR))
        user_or_movie1='{}'.format(user_or_movie)
        if simres==True:
            pass
        else:
            recco=getRecommendations(self.ratings, user_or_movie1, similarity=sim_distance)
            for key in recco:
                for s in recco[0]:
                    if s in self.ratings:
                        self.movie_ti.append(s)
            for item in self.movie_ti:
                self.lb2.insert(END,item)










    def uploadRatings(self):
        self.ratings={}
        i=1
        for line in open(r'C:\Users\aycakaya\Desktop\ratings.csv','r+'):
            if i==1:
                i+=1
                continue
            else:
                (userId,movieId,rating,timestamp)=line[0:-1].split(',')
                movie_rating=rating.split('"')[0]
                self.ratings.setdefault(userId,{})
                self.ratings[userId][movieId]=float(movie_rating)
        return self.ratings

    def uploadMovies(self):
        self.movies={}
        with open(r'C:\Users\aycakaya\Desktop\movies.csv', 'r', encoding='utf8') as fi:
            reader = csv.reader(fi,delimiter=',',quotechar=',')
            for i, row in enumerate(reader):
                if (len(row) < 1):
                    continue
                else:
                    self.movies[row[0]] = {row[1]}
            return self.movies

    def uploadLinks(self):
        self.link = {}
        with open(r'C:\Users\aycakaya\Desktop\links.csv', 'r', encoding='utf8') as fi:
            reader = csv.reader(fi, delimiter=',', quotechar=',')
            for i, row in enumerate(reader):
                if (len(row) < 1):
                    continue
                else:
                    self.link[row[0]] = {row[1]}
            return self.link

def main():
    root=Tk()
    root.geometry('730x500+420+150')
    root.title('Movie Rec. Eng.')
    g = Reco(root)
    root.mainloop()
main()

