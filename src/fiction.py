import tkinter

class fiction_books:
        def __init__(self,master):
                
                sciencefiction_btn=tkinter.Button(master,text='Science Fiction',command=self.showScienceFiction,width=15,relief=tkinter.RAISED)
                sciencefiction_btn.grid(row=1,column=1)
                satire_btn=tkinter.Button(master,text='Satire',command=self.showsatire,width=15,relief=tkinter.RAISED)
                satire_btn.grid(row=2,column=1)
                drama_btn=tkinter.Button(master,text='Drama',command=self.showdrama,width=15,relief=tkinter.RAISED)
                drama_btn.grid(row=3,column=1)
                adventure_btn=tkinter.Button(master,text='Adventure',command=self.showadventure,width=15,relief=tkinter.RAISED)
                adventure_btn.grid(row=4,column=1)
                romance_btn=tkinter.Button(master,text='Romance',command=self.showromance,width=15,relief=tkinter.RAISED)
                romance_btn.grid(row=5,column=1)
                mystery_btn=tkinter.Button(master,text='Mystery',command=self.showmystery,width=15,relief=tkinter.RAISED)
                mystery_btn.grid(row=6,column=1)
                poetry_btn=tkinter.Button(master,text='Poetry',command=self.showpoetry,width=15,relief=tkinter.RAISED)
                poetry_btn.grid(row=7,column=1)
                horror_btn=tkinter.Button(master,text='Horror',command=self.showhorror,width=15,relief=tkinter.RAISED)
                horror_btn.grid(row=8,column=1)
                comics_btn=tkinter.Button(master,text='Comics',command=self.showcomic,width=15,relief=tkinter.RAISED)
                comics_btn.grid(row=9,column=1)
                self.Lb1=tkinter.Listbox(master)
                self.Lb1.grid(row=1,column=2,rowspan=6)
        def put(self,lst):
                self.Lb1.delete(0,tkinter.END)
                for i in range(len(lst)):
                        self.Lb1.insert(i,lst[i])
        def showScienceFiction(self):
                lst=['All the Birds in the Sky by CHARLIE JANE ANDERS','Amatka by KARIN TIDBECK','Ammonite by NICOLA GRIFFITH','Anathem by NEAL STEPHENSON','Ancillary Justice by ANN LECKIE','The Best of All Possible Worlds by KAREN LORD','Binti by NNEDI OKORAFOR','Foundation by Isaac Asimov','Nineteen Eighty-Four by George Orwel','Odd John by Olaf Stapledon ']
                self.put(lst)
        def showsatire(self):

                lst=[' Brave New World by Aldous Huxley','The Hitchhiker’s Guide to the Galaxy by Douglas Adams','Don Quixote by Miguel de Cervantes','White Noise by Don DeLillo','The Pearl of Kuwait by Tom Paine','MASH by Richard Hooker','Machine Man by Max Barry','I Am America! And So Can You! by Stephen Colbert','The Adventures of Huckleberry Finn by Mark Twain','1984 by George Orwell']
                self.put(lst)
        def showdrama(self):

                lst=['Othello by William Shakespeare','Random Harvest: A Novel by James Hilton','Julius Caesar by William Shakespeare','The Good Luck Charm by Helena Hunting','A Raisin in the Sun by Lorraine Hansberry','The Perfect Couple by Elin Hilderbrand','Romeo and Juliet by William Shakespeare','The Crucible: A Play in Four Acts by Arthur Miller','The Kiss Quotient by Helen Hoang','Hamilton: The Revolution by Lin-Manuel Miranda']
                self.put(lst)
        def showadventure(self):

                lst=['THE RAVEN BOYS BY MAGGIE STIEFVATER','FINNIKIN OF THE ROCK BY MELINA MARCHETTA','SHADOWSHAPER BY DANIEL JOSÉ OLDER','AMERICAN GODS BY NEIL GAIMAN','MR. PENUMBRA’S 24-HOUR BOOKSTORE BY ROBIN SLOAN','LIFE OF PI BY YANN MARTEL','READY PLAYER ONE BY ERNEST CLINE','THE LIMINAL WAR BY AYIZE JAMA-EVERETT','THE DARKEST PART OF THE FOREST BY HOLLY BLACK','ESCAPE FROM BAGHDAD BY SAAD Z. HOSSAIN']
                self.put(lst)
        def showromance(self):

                lst=['WHEN DIMPLE MET RISHI BY SANDHYA MENON','EVERYTHING LEADS TO YOU BY NINA LACOUR','MY SO-CALLED BOLLYWOOD LIFE BY NISHA SHARMA','AUTOBOYOGRAPHY BY CHRISTINA LAUREN','ANNA AND THE FRENCH KISS BY STEPHANIE PERKINS','THE SUMMER OF JORDI PEREZ (AND THE BEST BURGER IN LOS ANGELES) BY AMY SPALDING','TO ALL THE BOYS I’VE LOVED BEFORE BY JENNY HAN','THE SUN IS ALSO A STAR BY NICOLA YOON','JUST ONE DAY BY GAYLE FORMAN','THIS LULLABY BY SARAH DESSEN']
                self.put(lst)
        def showmystery(self):

                lst=['The 7 ½ Deaths of Evelyn Hardcastle by Stuart Turton','EVERYTHING I NEVER TOLD YOU BY CELESTE NG','WHITE TEARS BY HARI KUNZRU','REBECCA BY DAPHNE DU MAURIER','MR. PENUMBRA’S 24-HOUR BOOKSTORE BY ROBIN SLOAN','THE HIDDEN KEYS BY ANDRÉ ALEXIS','BEHIND THE SCENES AT THE MUSEUM BY KATE ATKINSON','THE DISTANT HOURS BY KATE MORTON','SNOW FALLING ON CEDARS BY DAVID GUTERSON','THE BOOK HUNTERS OF KATPADI BY PRADEEP SEBASTIAN']
                self.put(lst)
        def showpoetry(self):

                lst=['Blue Laws by Kevin Young','The Unaccompanied by Simon Armitage','bone by Yrsa Daley-Ward','Love in the Last Days by D. Nurkse','Poet in Spain by Federico García Lorca','The Rain in Portugal by Billy Collins','Devotions by Mary Oliver','Voyage of the Sable Venus by Robin Coste Lewis','The Surveyors by Mary Jo Salter','Electric Arches by Eve L. Ewing']
                self.put(lst)
        def showhorror(self):

                lst=['AFFINITY BY SARAH WATERS','AT THE MOUNTAINS OF MADNESS BY H.P. LOVECRAFT','AUDITION BY RYU MURAKAMI','THE BAD SEED BY WILLIAM MARCH','BELOVED BY TONI MORRISON','THE BETWEEN BY TANANARIVE DUE','BOY’S LIFE BY ROBERT R. MCCAMMON','CARMILLA BY J. SHERIDAN LE FANU','THE DEVIL IN SILVER BY VICTOR LAVALLE','DRACULA BY BRAM STOKER']
                self.put(lst)
        def showcomic(self):

                lst=['Astonishing X-Men','Justice League Of America','New Avengers','Batman','Amazing Spider Man','Action Comics','The Incredible Hulk','Wolverine','The Ultimates','Teen Titans']
                self.put(lst)
                
if __name__=='__main__':
    master=tkinter.Tk()
    fiction_books(master)
    master.mainloop()


