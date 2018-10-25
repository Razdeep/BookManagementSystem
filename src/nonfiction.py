import tkinter

class nonfiction_books:
        def __init__(self,master):
                master.config(bg="peach puff")
                sciencefiction_btn=tkinter.Button(master,text='Science',bg="peach puff",font=('Comic Sans MS',18),command=self.showScience,width=13,relief=tkinter.RAISED)
                sciencefiction_btn.grid(row=1,column=1)
                satire_btn=tkinter.Button(master,text='History',bg="peach puff",font=('Comic Sans MS',18),command=self.showHistory,width=13,relief=tkinter.RAISED)
                satire_btn.grid(row=2,column=1)
                drama_btn=tkinter.Button(master,text='Anthology',bg="peach puff",font=('Comic Sans MS',18),command=self.showAnthology,width=13,relief=tkinter.RAISED)
                drama_btn.grid(row=3,column=1)
                adventure_btn=tkinter.Button(master,text='Maths',bg="peach puff",font=('Comic Sans MS',18),command=self.showMaths,width=13,relief=tkinter.RAISED)
                adventure_btn.grid(row=4,column=1)
                romance_btn=tkinter.Button(master,text='Health',bg="peach puff",font=('Comic Sans MS',18),command=self.showHealth,width=13,relief=tkinter.RAISED)
                romance_btn.grid(row=5,column=1)
                mystery_btn=tkinter.Button(master,text='Travel',bg="peach puff",font=('Comic Sans MS',18),command=self.showTravel,width=13,relief=tkinter.RAISED)
                mystery_btn.grid(row=6,column=1)
                poetry_btn=tkinter.Button(master,text='Encyclopedias',bg="peach puff",font=('Comic Sans MS',18),command=self.showEncyclopedias,width=13,relief=tkinter.RAISED)
                poetry_btn.grid(row=7,column=1)
                horror_btn=tkinter.Button(master,text='Biographies',bg="peach puff",font=('Comic Sans MS',18),command=self.showBiographies,width=13,relief=tkinter.RAISED)
                horror_btn.grid(row=8,column=1)
                comics_btn=tkinter.Button(master,text='Autobiographies',bg="peach puff",font=('Comic Sans MS',18),command=self.showAutobiographies,width=13,relief=tkinter.RAISED)
                comics_btn.grid(row=9,column=1)
                self.Lb1=tkinter.Listbox(master,width=25,height=30)
                self.Lb1.grid(row=1,column=2,rowspan=12)
        def put(self,lst):
                self.Lb1.delete(0,tkinter.END)
                for i in range(len(lst)):
                        self.Lb1.insert(i,lst[i])
        def showScience(self):
                lst=['The War of The Worlds','The Universe in a Single Atom','Make It Stick','The Science of Interstellar ','Social Intelligence','The Time Machine','Enlightenment Now','Why We Buy','On Food and Cooking','Unlimited Power','Undeniable','Superforecasting','Genius','The Science of Discworld ','The Gay Science','Chaos','Bonk','Animal Farm','Bad Science','Silent Spring','The First Three Minutes','The Cosmic Connection','The Double Helix','The Selfish Gene','Relativity','Physica','De Revolution','Dialogue']
                self.put(lst)
        def showHistory(self):

                lst=['Napoleon the Great','Night Walking ','Magna Carta',' Men at War','Stalins Englishman','The Sea and Civilisation','Beautiful Idiots and Brilliant Lunatics','Headstrong','SPQR','The English and Their History','Asoka and the Decline of the Mauryas','Somanatha','Alberunis India','An Era of Darkness','Borders and Boundaries','Pink Sari Revolution','Women of the Raj','The Madurai Sultanate','The Origins of Yoga and Tantra','Ancient India','Sacred River','Dalit Visions','South India Under the Cholas','Women of the Raj','Maharaja','The Mulberry Empire','We Also Made History','India Unbound','Farewell The Trumpets']
                self.put(lst)
        def showAnthology(self):

                lst=['Peel Back the Skin','Feeling Very Strange','The Bhagavad Gita','Dark Fates','Snows of Darkover','BookElves Anthology Volume 2 ','Behind the Mask','The Anthology of Rap ','A Mind Awake','The Essential Gandhi','True Crime','Color of Violence','Art of War','The Chronicles of Narnia','Bend','Gamlet','A Zombie Anthology ','Mirrorshades','Doubletakes','Supernatural Noir','The Anchor Book','The Vintage Book','The Best American Nonrequired Reading','New Stories from the South','The Pushcart Prize','The O’Henry Prize Stories','The Year’s Best Science Fiction and Fantasy','The Year’s Best Dark Fantasy and Horror']
                self.put(lst)
        def showMaths(self):

                lst=['Equal Shmequal','Games for Math ','Survival Math','How to Teach Your Baby Math ','Maths in Minutes','Tyrannosaurus Math ','Math for Grownups','A Rolling Stone Gathers No Moss ','Math Does not Suck','The Math Olympian ','New Math is Murder','Math Girls ','The Grapes of Math','Fooling Houdini','The Boy Who Loved Math','Fluke','Math and the Mona Lisa ','The Quants','The Magic of Math','Classic Set Theory','Mathematics and its History','Mathematics','Categories for the Working Mathematician','Encyclopedia of Mathematics','The Princeton Companion to Mathematics','Principles and Techniques in Combinatorics','Calculus Made Easy','Abstract Algebra','Contemporary Abstract Algebra']
                self.put(lst)
        def showHealth(self):

                lst=['The Power of No','The World Peace Diet','Typhoid Mary','Diet for a New America','Earthing','The Starch Solution','Integrative Nutrition','Health at Every Size','Eat for Health','Pathologies of Power','Zoobiquity','Switch On Your Brain','Dianetics','Food Politics','Practical Paleo','Money, and the Law of Attraction','The Story of the Human Body','Forks Over Knives','Wheat Belly','Judgment Detox','The Yes Brain','We Flow Hard','The Year of Less','Judgment Detox','Metabolism Revolution','The Better Brain Solution','Power Plates','The Nalini Method','Big Girl']
                self.put(lst)
        def showTravel(self):

                lst=['Time Travel in Einsteins Universe','The Jaunt. Travel ','The Travelling Bag ','Traveling Light','Gullivers Travel ','An Idiot Abroad','Travel as a Political Act ','Traveling with Pomegranates','The Dead Travel Fast','I am Traveling Alone','The Dead Travel Fast ','Treasure Island','Questions of Travel ','Metamorphosis','Vagabonding','The Traveling Vampire Show ','Traveling Mercies','Doomsday Book','The Art of Travel ','The Geography of Bliss','In A Sunburned Country','Vagabonding','The Beach','The Lost City of Z','Unlikely Destinations','On the Road','The Caliph’s House','Love With a Chance of Drowning','The Alchemist']
                self.put(lst)
        def showEncyclopedias(self):

                lst=['The Cambridge Encyclopedia of Language ','Fantasy Encyclopedia ','Mozipedia','Encyclopedia Brown Saves the Day ','WWE Encyclopedia ','The Element Encyclopedia of Witchcraft ','Fables','The Star Trek Encyclopedia ','The DC Comics Encyclopedia ','The Encyclopedia of Country Living ','The A to Z Encyclopedia of Serial Killers ','The Vampire Book','The Encyclopedia of Serial Killers ','Encyclopedia Brown Finds the Clues','The Dune Encyclopedia ','The Great Encyclopedia of Faeries ','The Encyclopedia of the Dead ','Encyclopedia of an Ordinary Life ','Encyclopedia Brown, Boy Detective','Hutchinson Encyclopedia','In the Presence of Dinosaurs','Great Soviet Encyclopedia','Feathered Dinosaurs','Encyclopaedia Sinica','Dinosaur Encyclopedia','Colliers Encyclopedia','Christelijke Encyclopedie','British Encyclopaedia','Burmese Encyclopedia']
                self.put(lst)
        def showBiographies(self):

                lst=['Room Full of Mirrors','Woodrow Wilson','Macbeth','Schulz and Peanuts','The Bible','The Secret Garden','The Count of Monte Cristo','Shakey','Muhammad','Dracula','Steve Jobs','Jane Eyre','Zero','Heavier Than Heaven','J.R.R. Tolkien','The Beatles','Jerusalem','Jim Henson','Frida','The Emperor of All Maladies','Hellfire','Churchill','The Kid Stays In The Picture','Darwin','The Moon’s A Balloon','Jackson Pollock','Kitchen Confidential','Muhammad Ali','Titan','A Moveable Feast']
                self.put(lst)
        def showAutobiographies(self):

                lst=['The Measure of a Man','Le Journal d Anne Frank ','Iacocca','Autobiography of a Yogi ','Boy: Tales of Childhood','Neil Patrick Harris','The Autobiography of Martin Luther King, Jr.','Pioneer Girl','My Autobiography ','Kaffir Boy','American Sniper','Clapton','Miles','Assata','Wings of Fire','My Experiments with Truth','The Autobiography of Malcolm X ','Autobiography of Red ','Autobiography of a Face ','The Autobiography of Benjamin Franklin ','My Music, My Life','My Struggles','The Insider','My Days','My Reminiscences','My Presidential Years','My Own Boswell','My Life and Times','An Autobiography']
                self.put(lst)
                
if __name__=='__main__':
    master=tkinter.Tk()
    nonfiction_books(master)
    master.mainloop()



