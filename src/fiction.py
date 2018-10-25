import tkinter

class fiction_books:
        def __init__(self,master):
                master.config(bg="OliveDrab1")
                sciencefiction_btn=tkinter.Button(master,text='Science Fiction',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showScienceFiction,width=13,relief=tkinter.RAISED)
                sciencefiction_btn.grid(row=1,column=1)
                satire_btn=tkinter.Button(master,text='Satire',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showsatire,width=13,relief=tkinter.RAISED)
                satire_btn.grid(row=2,column=1)
                drama_btn=tkinter.Button(master,text='Drama',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showdrama,width=13,relief=tkinter.RAISED)
                drama_btn.grid(row=3,column=1)
                adventure_btn=tkinter.Button(master,text='Adventure',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showadventure,width=13,relief=tkinter.RAISED)
                adventure_btn.grid(row=4,column=1)
                romance_btn=tkinter.Button(master,text='Romance',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showromance,width=13,relief=tkinter.RAISED)
                romance_btn.grid(row=5,column=1)
                mystery_btn=tkinter.Button(master,text='Mystery',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showmystery,width=13,relief=tkinter.RAISED)
                mystery_btn.grid(row=6,column=1)
                poetry_btn=tkinter.Button(master,text='Poetry',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showpoetry,width=13,relief=tkinter.RAISED)
                poetry_btn.grid(row=7,column=1)
                horror_btn=tkinter.Button(master,text='Horror',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showhorror,width=13,relief=tkinter.RAISED)
                horror_btn.grid(row=8,column=1)
                comics_btn=tkinter.Button(master,text='Comics',bg="OliveDrab2",font=('Comic Sans MS',18),command=self.showcomic,width=13,relief=tkinter.RAISED)
                comics_btn.grid(row=9,column=1)
                self.Lb1=tkinter.Listbox(master,width=25,height=30)
                self.Lb1.grid(row=1,column=2,rowspan=12)
        def put(self,lst):
                self.Lb1.delete(0,tkinter.END)
                for i in range(len(lst)):
                        self.Lb1.insert(i,lst[i])
        def showScienceFiction(self):
                lst=['The Adversary','Parallax','Omni-Man','Annihilus','Omega Red','Despero','Violator','Mastermind','MODOK','Fin Fang Foom','Moon Knight','Astonishing X-Men','Justice League Of America','New Avengers','Batman','Amazing Spider Man','Action Comics','The Incredible Hulk','Wolverine','The Ultimates','Teen Titans','All the Birds in the Sky ','Amatka ','Ammonite','Anathem','Ancillary Justice','The Best of All Possible Worlds','Binti','Foundation','Nineteen Eighty-Four','Odd John']
                self.put(lst)
        def showsatire(self):

                lst=['The Adversary','Parallax','Omni-Man','Annihilus','Omega Red','Despero','Violator','Mastermind','MODOK','Fin Fang Foom','Moon Knight','Astonishing X-Men','Justice League Of America','Stars','You are in','Attack of the Movies','After All?','Screening at Stores','GDC 2005','E3 2005','Preview','Designed for Fame','ECTS 2003','Canned','High Res','Activision',' Brave New World','Guide to the Galaxy','Don Quixote','White Noise','The Pearl of Kuwait','MASH','Machine Man','I Am America! ','The Adventures of Huckleberry','1984 ']
                self.put(lst)
        def showdrama(self):

                lst=['Home Movies','The 7 ½ Deaths of Evelyn Hardcastle','EVERYTHING I NEVER TOLD YOU','WHITE TEARS','REBECCA','MR. PENUMBRA’S 24-HOUR BOOKSTORE','THE HIDDEN KEYS','BEHIND THE SCENES AT THE MUSEUM KINSON','Why Mummy Swears','Anatomy of a Scandal','Kintu','An Unsuitable Match','A Ration Book Christmas','The Year That Changed Everything','Trap','The Mum Who Had Enough','The Lion Tamer Who Lost','Othello','Random Harvest','Julius Caesar','The Good Luck Charm','A Raisin in the Sun','The Perfect Couple','Romeo and Juliet','The Crucible','The Kiss Quotient','Hamilton']
                self.put(lst)
        def showadventure(self):

                lst=['The Adversary','Parallax','Omni-Man','Annihilus','Omega Red','Despero','Violator','Mastermind','MODOK','Fin Fang Foom','Moon Knight','Astonishing X-Men','Justice League Of America','New Avengers','Batman','Amazing Spider Man','Action Comics','The Incredible Hulk','Wolverine','The Ultimates','Teen Titans','THE RAVEN BOYS','FINNIKIN OF THE ROCK','SHADOWSHAPER','AMERICAN GODS','MR. PENUMBRAS BOOKSTORE','LIFE OF PI','READY PLAYER ONE','THE LIMINAL WAR','THE DARKEST PART OF THE FOREST','ESCAPE FROM BAGHDAD']
                self.put(lst)
        def showromance(self):

                lst=['THE SUMMER OF SLOANE','99 DAYS','THE HEARTBREAKERS','THE WEIGHT OF FEATHERS','PLAIN VANILLA','THE DISTANCE FROM A TO Z','LETTERS TO THE LOST ','THE VICTORIA IN MY HEAD ','LIVING VIOLET','THE SUMMER OF US','The Family Tabor','IF I WAS YOUR GIRL','FIVE STAR BILLIONAIRE','THE INCARNATIONS ','LOVE MEDICINE ','BEHOLD THE DREAMERS','SONG OF SOLOMON','EVERYTHING I NEVER TOLD YOU ','AMERICANAH','THERE THERE ','WHEN DIMPLE MET RISHI','EVERYTHING LEADS TO YOU','MY SO-CALLED BOLLYWOOD LIFE','AUTOBOYOGRAPHY','ANNA AND THE FRENCH KISS','THE SUMMER OF JORDI PEREZ','TO ALL THE BOYS I’VE LOVED BEFORE','THE SUN IS ALSO A STAR','JUST ONE DAY','THIS LULLABY']
                self.put(lst)
        def showmystery(self):

                lst=['Stunts & Effects','Stars','You are in','Attack of the Movies','After All?','Screening at Stores','GDC 2005','E3 2005','Preview','Designed for Fame','ECTS 2003','Canned','High Res','Activision','Zombiemania','The New Scooby-Doo Movies','Star Wars','The Librarian','Home Movies','The 7 ½ Deaths of Evelyn Hardcastle','EVERYTHING I NEVER TOLD YOU','WHITE TEARS','REBECCA','MR. PENUMBRA’S 24-HOUR BOOKSTORE','THE HIDDEN KEYS','BEHIND THE SCENES AT THE MUSEUM KINSON','THE DISTANT HOURS','SNOW FALLING ON CEDARS','THE BOOK HUNTERS OF KATPADI']
                self.put(lst)
        def showpoetry(self):

                lst=['Dead Poets Society','Public Opinions Needed','Fire Pro Wrestling for Dreamcast','Short Term','Videogame','Dark Poetry','War poetry','Tactical Nuke ','To the Amazonians','The Lost Tapes','One Time','Poetry corner','A little poetry','The Fred Hembeck Show','Capote','Supernatural','Poetry Slam','Poetry in Motion','Out of This World','Blue Laws','The Unaccompanied','bone','Love in the Last Days','Poet in Spain','The Rain in Portugal','Devotions','Voyage of the Sable Venus','The Surveyors','Electric Arches']
                self.put(lst)
        def showhorror(self):

                lst=['A Christmas','Chocolate','Home','Gift Ideas','Overall','Trivia','Alone','Flick','The Horror! The Horror!','The Lurking Horror','Horror Night!','Shuffling Horror','Spectral','Princess of Horror','The Amityville Horror','Silent Hill Mobile','Summon Horror','Jason Blum On the Stigma of Horror ','Masters of Horror','American Horror Story','AFFINITY','AT THE MOUNTAINS OF MADNESS','AUDITION','THE BAD SEED','BELOVED','THE BETWEEN','BOYS LIFE','CARMILLA','THE DEVIL IN SILVER','DRACULA']
                self.put(lst)
        def showcomic(self):

                lst=['Grigori Rasputin','Doctor Light','Mysterio','The Govenor','Electro','Hunter Rose','Shade','Carnage','The Adversary','Parallax','Omni-Man','Annihilus','Omega Red','Despero','Violator','Mastermind','MODOK','Fin Fang Foom','Moon Knight','Astonishing X-Men','Justice League Of America','New Avengers','Batman','Amazing Spider Man','Action Comics','The Incredible Hulk','Wolverine','The Ultimates','Teen Titans']
                self.put(lst)
                
if __name__=='__main__':
    master=tkinter.Tk()
    fiction_books(master)
    master.mainloop()



