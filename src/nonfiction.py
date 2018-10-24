import tkinter

class nonfiction_books:
        def __init__(self,master):
                
                sciencefiction_btn=tkinter.Button(master,text='Science',command=self.showScience,width=15,relief=tkinter.RAISED)
                sciencefiction_btn.grid(row=1,column=1)
                satire_btn=tkinter.Button(master,text='History',command=self.showHistory,width=15,relief=tkinter.RAISED)
                satire_btn.grid(row=2,column=1)
                drama_btn=tkinter.Button(master,text='Anthology',command=self.showAnthology,width=15,relief=tkinter.RAISED)
                drama_btn.grid(row=3,column=1)
                adventure_btn=tkinter.Button(master,text='Maths',command=self.showMaths,width=15,relief=tkinter.RAISED)
                adventure_btn.grid(row=4,column=1)
                romance_btn=tkinter.Button(master,text='Health',command=self.showHealth,width=15,relief=tkinter.RAISED)
                romance_btn.grid(row=5,column=1)
                mystery_btn=tkinter.Button(master,text='Travel',command=self.showTravel,width=15,relief=tkinter.RAISED)
                mystery_btn.grid(row=6,column=1)
                poetry_btn=tkinter.Button(master,text='Encyclopedias',command=self.showEncyclopedias,width=15,relief=tkinter.RAISED)
                poetry_btn.grid(row=7,column=1)
                horror_btn=tkinter.Button(master,text='Biographies',command=self.showBiographies,width=15,relief=tkinter.RAISED)
                horror_btn.grid(row=8,column=1)
                comics_btn=tkinter.Button(master,text='Autobiographies',command=self.showAutobiographies,width=15,relief=tkinter.RAISED)
                comics_btn.grid(row=9,column=1)
                self.Lb1=tkinter.Listbox(master)
                self.Lb1.grid(row=1,column=2,rowspan=6)
        def put(self,lst):
                self.Lb1.delete(0,tkinter.END)
                for i in range(len(lst)):
                        self.Lb1.insert(i,lst[i])
        def showScience(self):
                lst=['Silent Spring by Rachel Carson','The First Three Minutes by Steven Weinberg','The Cosmic Connection by Carl Sagan','The Cosmic Connection by Carl Sagan','The Double Helix by James D. Watson','The Selfish Gene by Richard Dawkins ','Relativity: The Special and General Theory by Albert Einstein ','Physica by Aristotle','De Revolutionibus Orbium Coelestium by Nicolaus Copernicus','Dialogue Concerning the Two Chief World Systems by Galileo Galilei']
                self.put(lst)
        def showHistory(self):

                lst=['Napoleon the Great by Andrew Roberts','Night Walking by Matthew Beaumont','Magna Carta by David Starkey',' Men at War: What Fiction Tells us About Conflict, From The Iliad to Catch-22 by Christopher Coker','Stalins Englishman by Andrew Lownie','The Sea and Civilisation: A Maritime History of the World by Lincoln Paine','Beautiful Idiots and Brilliant Lunatics by Rob Baker','Headstrong - 52 Women Who Changed Science and the World by Rachel Swaby','SPQR: A History of Ancient Rome by Mary Beard','The English and Their History by Robert Tombs']
                self.put(lst)
        def showAnthology(self):

                lst=['Doubletakes, edited by T.C. Boyle','Supernatural Noir, edited by Ellen Datlow','The Anchor Book of New American Short Stories, edited by Ben Marcus','The Vintage Book of Contemporary American Short Stories, edited by Tobias Wolff','The Best American Nonrequired Reading (annual), edited by Dave Eggers','New Stories from the South: The Years Best (annual), Kathy Pories, series editor','The Pushcart Prize: Best of the Small Presses (annual), edited by Bill Henderson','The O’Henry Prize Stories (annual), Laura Furman, series editor','The Year’s Best Science Fiction and Fantasy (annual), edited by Rich Horton','The Year’s Best Dark Fantasy and Horror (annual), edited by Paula Guran']
                self.put(lst)
        def showMaths(self):

                lst=['Classic Set Theory for Guided Independent Study by Derek C. Goldrei','Mathematics and its History by John Stillwell','Mathematics: From the Birth of Numbers by Jan Gullberg','Categories for the Working Mathematician by Saunders Mac Lane','Encyclopedia of Mathematics by James Stuart Tanton','The Princeton Companion to Mathematics by Timothy Gower','Principles and Techniques in Combinatorics by Chen Chuan-Chong and Koh Khee-Meng','Calculus Made Easy by Silvanus P. Thompson','Abstract Algebra by David S. Dummi','Contemporary Abstract Algebra by Joseph Gallia']
                self.put(lst)
        def showHealth(self):

                lst=['Judgment Detox by Gabrielle Bernstein','The Yes Brain by Daniel J. Siegel, MD and Tina Payne Bryson','We Flow Hard by Sarah and Mason Levey','The Year of Less by Cait Flanders','Judgment Detox by Gabrielle Bernstein','Metabolism Revolution by Haylie Pomroy','The Better Brain Solution by Steven Masley','Power Plates by Gena Hamshaw','The Nalini Method: 7 Workouts for 7 Moods by Rupa Mehta','Big Girl: How I Gave Up Dieting and Got a Life by Kelsey Miller']
                self.put(lst)
        def showTravel(self):

                lst=['The Geography of Bliss, by Eric Weiner','In A Sunburned Country, by Bill Bryson','Vagabonding, by Rolf Potts','The Beach, by Alex Garland','The Lost City of Z, by David Grann','Unlikely Destinations: The LP Story, by Tony & Maureen Wheeler','On the Road, by Jack Kerouac','The Caliph’s House: A Year in Casablanca by Tahir Shah','Love With a Chance of Drowning, by Torre DeRoche','The Alchemist by Paulo Coelho']
                self.put(lst)
        def showEncyclopedias(self):

                lst=['Hutchinson Encyclopedia','In the Presence of Dinosaurs','Great Soviet Encyclopedia','Feathered Dinosaurs: The Origin of Birds','Encyclopaedia Sinica','Dinosaur Encyclopedia','Colliers Encyclopedia','Christelijke Encyclopedie','British Encyclopaedia','Burmese Encyclopedia']
                self.put(lst)
        def showBiographies(self):

                lst=['Hellfire: The Jerry Lee Lewis Story by Nick Tosches','Churchill: A Life by Martin Gilbert','The Kid Stays In The Picture: A Notorious Life by Robert Evans','Darwin: The Life Of A Tortured Evolutionist by Adrian Desmond and James Moore','The Moon’s A Balloon by David Niven','Jackson Pollock: An American Saga by Steven Naifeh & Gregory White Smith','Kitchen Confidential: Adventures In The Culinary Underbelly by Anthony Bourdain','Muhammad Ali: His Life And Times by Thomas Hauser','Titan: The Life Of John D Rockefeller Sr by Ron Chernow','A Moveable Feast by Ernest Hemingway']
                self.put(lst)
        def showAutobiographies(self):

                lst=['My Experiments with Truth	by Mahatma Gandhi','My Music, My Life by Pt. Ravi Shankar','My Struggles by E.K. Nayanar','The Insider by P.V. Narasimha Rao','My Days by R.K. Narayan','My Reminiscences by R.N. Tagore','My Presidential Years by R. Vekatataman','My Own Boswell: Memoirs by M. Hidayatullah','My Life and Times by V.V. Giri','An Autobiography by Jawaharlal Nehru']
                self.put(lst)
                
if __name__=='__main__':
    master=tkinter.Tk()
    nonfiction_books(master)
    master.mainloop()


